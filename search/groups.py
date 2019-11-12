from search.utility import get_match_score
from enum import Enum


class GroupsAttributes(Enum):
    id = 'id'
    name = 'name'
    description = 'description'

class Groups:
    searchable_attributes_list = [GroupsAttributes.name.value, GroupsAttributes.description.value]
    transitive_searchable_fields_list = [GroupsAttributes.name.value]
    weight_dictionary = {
        GroupsAttributes.name.value: 9,
        GroupsAttributes.description.value: 5
    }

    def __init__(self, groups):
        self.groups = groups

    def get_all_groups(self):
        return self.groups

    def _is_valid_attribute_value(self, value):
        if value is None:
            return False
        return True

    def get_most_relevant_results(self, query_text, score_threshold=0):
        results = []
        transitive_attribute_contribution = {
            GroupsAttributes.name.value: 0
        }
        for group in self.groups:
            # print('group: ', group)
            match_score = 0
            for attribute in self.searchable_attributes_list:
                # print('attribute: ', attribute)
                if not self._is_valid_attribute_value(group[attribute]):
                    continue
                attribute_score = get_match_score(query_text, group[attribute])
                if attribute_score >= 1 and attribute in self.transitive_searchable_fields_list:
                    transitive_attribute_contribution[attribute] += attribute_score
                match_score = match_score + (attribute_score * self.weight_dictionary[attribute])
            if match_score > score_threshold:
                results.append([group, match_score])
        return results
