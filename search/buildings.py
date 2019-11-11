from search.utility import get_match_score
from enum import Enum


class BuildingAttributes(Enum):
    id = 'id'
    shortCut = 'shortCut'
    name = 'name'
    description = 'description'


class Buildings:
    searchable_attributes_list = [BuildingAttributes.shortCut.value, BuildingAttributes.name.value, BuildingAttributes.description.value]
    weight_dictionary = {
        BuildingAttributes.shortCut.value: 7,
        BuildingAttributes.name.value: 9,
        BuildingAttributes.description.value: 5
    }

    def __init__(self, buildings):
        self.buildings = buildings
        print('Buildings imported')

    def get_all_buildings(self):
        return self.buildings

    def get_most_relevant_results(self, query_text, score_threshold=0):
        results = []
        for building in self.buildings:
            # print('building: ', building)
            match_score = 0
            for attribute in self.searchable_attributes_list:
                # print('attribute: ', attribute)
                match_score = match_score + (get_match_score(query_text, building[attribute]) * self.weight_dictionary[attribute])
                if match_score > score_threshold:
                    results.append([building, match_score])
        return results
