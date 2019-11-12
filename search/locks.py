from search.utility import get_match_score
from enum import Enum


class LocksAttributes(Enum):
    id = 'id'
    buildingId = 'buildingId'
    type = 'type'
    name = 'name'
    serialNumber = 'serialNumber'
    floor = 'floor'
    roomNumber = 'roomNumber'
    description = 'description'


class Locks:
    searchable_attributes_list = [LocksAttributes.type.value, LocksAttributes.name.value, LocksAttributes.serialNumber.value, LocksAttributes.floor.value, LocksAttributes.roomNumber.value, LocksAttributes.description.value]
    transitive_field_list = [LocksAttributes.buildingId.value]
    weight_dictionary = {
        LocksAttributes.type.value: 3,
        LocksAttributes.name.value: 10,
        LocksAttributes.serialNumber.value: 8,
        LocksAttributes.floor.value: 6,
        LocksAttributes.roomNumber.value: 6,
        LocksAttributes.description.value: 6
    }

    def __init__(self, locks):
        self.locks = locks

    def get_all_locks(self):
        return self.locks

    def _is_valid_attribute_value(self, value):
        if value is None:
            return False
        return True

    def get_most_relevant_results(self, query_text, transitive_fields_contribution = {}, score_threshold=0):
        results = []
        for lock in self.locks:
            match_score = 0
            for attribute in self.searchable_attributes_list:
                if not self._is_valid_attribute_value(lock[attribute]):
                    continue
                attribute_score = get_match_score(query_text, lock[attribute])
                match_score = match_score + (attribute_score * self.weight_dictionary[attribute])

            lock_id = lock[LocksAttributes.buildingId.value]
            if lock_id in transitive_fields_contribution:
                match_score  = match_score + transitive_fields_contribution[lock_id]
            if match_score > score_threshold:
                results.append([lock, match_score])
        return results
