from search.utility import get_match_score
from enum import Enum


class BuildingAttributes(Enum):
    id = 'id'
    shortCut = 'shortCut'
    name = 'name'
    description = 'description'


class Buildings:
    searchable_attributes_list = [BuildingAttributes.shortCut.value, BuildingAttributes.name.value, BuildingAttributes.description.value]
    transitive_searchable_fields_list = [BuildingAttributes.shortCut.value, BuildingAttributes.name.value]
    weight_dictionary = {
        BuildingAttributes.shortCut.value: 7,
        BuildingAttributes.name.value: 9,
        BuildingAttributes.description.value: 5
    }
    transitive_weight_dictionary = {
        BuildingAttributes.shortCut.value: 5,
        BuildingAttributes.name.value: 8
    }

    def __init__(self, buildings):
        self.buildings = buildings
        print('Buildings imported')

    def get_all_buildings(self):
        return self.buildings

    def get_most_relevant_results(self, query_text, score_threshold=0):
        results = []
        transitive_attribute_contribution_ids = {}
        for building in self.buildings:
            # print('building: ', building)
            match_score = 0
            for attribute in self.searchable_attributes_list:
                attribute_score = get_match_score(query_text, building[attribute])
                # print('attribute: ', attribute, ' score: ', attribute_score)
                if attribute_score >= 1 and attribute in self.transitive_searchable_fields_list:
                    building_id =  building[BuildingAttributes.id.value]
                    weighted_score = self.transitive_weight_dictionary[attribute] * attribute_score
                    if building_id in transitive_attribute_contribution_ids:
                        transitive_attribute_contribution_ids[building_id] += weighted_score
                    else:
                        transitive_attribute_contribution_ids[building_id] = weighted_score
                match_score = match_score + (attribute_score * self.weight_dictionary[attribute])

            if match_score > score_threshold:
                results.append([building, match_score])
        return results, transitive_attribute_contribution_ids
