import json

from search.buildings import Buildings
from search.groups import Groups
from search.locks import Locks
from search.media import Media

file_location = '../sv_lsm_data.json'

def deserialize_data_from_disk(json_location):
    file_mode = 'r'
    with open(json_location, file_mode) as read_file:
        data = json.load(read_file)
        return data


def get_top_k_results(num_results):
    data = deserialize_data_from_disk(file_location)

    buildings = data['buildings']
    buildings_obj = Buildings(buildings)

    locks = data['locks']
    locks_obj = Locks(locks)

    groups = data['groups']
    groups_obj = Groups(groups)

    media = data['media']
    media_obj = Media(media)

    relevant_entries, transitive_weight_from_buildings = buildings_obj.get_most_relevant_results('HOFF', 3)
    for entry in relevant_entries:
        print(entry)
    print(transitive_weight_from_buildings)

    relevant_entries = locks_obj.get_most_relevant_results('Cylinder', transitive_weight_from_buildings, 0)
    # print(relevant_entries)
    # for entry in relevant_entries:
    #     print(entry)


get_top_k_results(10)
