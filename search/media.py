
from search.utility import get_match_score, _is_valid_attribute_value
from enum import Enum


class MediasAttributes(Enum):
    id = 'id'
    groupId = 'groupId'
    type = 'type'
    owner = 'owner'
    serialNumber = 'serialNumber'
    description = 'description'


class Media:
    def __init__(self, media):
        self.media = media

    def get_all_media(self):
        return self.media

    searchable_attributes_list = [MediasAttributes.type.value, MediasAttributes.owner.value, MediasAttributes.serialNumber.value, MediasAttributes.description.value]
    transitive_field_list = [MediasAttributes.groupId.value]
    weight_dictionary = {
        MediasAttributes.type.value: 3,
        MediasAttributes.owner.value: 10,
        MediasAttributes.serialNumber.value: 8,
        MediasAttributes.description.value: 6
    }

    def get_most_relevant_results(self, query_text, transitive_fields_contribution = {}, score_threshold=0):
        results = []
        for m in self.media:
            match_score = 0
            for attribute in self.searchable_attributes_list:
                if not _is_valid_attribute_value(m[attribute]):
                    continue
                attribute_score = get_match_score(query_text, m[attribute])
                match_score = match_score + (attribute_score * self.weight_dictionary[attribute])

            media_id = m[MediasAttributes.groupId.value]
            if media_id in transitive_fields_contribution:
                match_score  = match_score + transitive_fields_contribution[media_id]
            if match_score > score_threshold:
                results.append([m, match_score])
        return results
