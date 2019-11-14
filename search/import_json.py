import json

from search.buildings import Buildings
from search.groups import Groups
from search.locks import Locks
from search.media import Media

from operator import itemgetter


def deserialize_data_from_disk(json_location):
    file_mode = 'r'
    with open(json_location, file_mode) as read_file:
        data = json.load(read_file)
        return data


def get_top_k_results(buildings_obj, locks_obj, groups_obj, media_obj, search_string, num_results=10):
    tok_k_results = []
    relevant_entries, transitive_weight_from_buildings = buildings_obj.get_most_relevant_results(search_string, 3)

    for entry in relevant_entries:
        entry.append('building')
        tok_k_results.append(entry)

    relevant_entries = locks_obj.get_most_relevant_results(search_string, transitive_weight_from_buildings, 0)
    for entry in relevant_entries:
        entry.append('lock')
        tok_k_results.append(entry)

    relevant_entries, transitive_weight_from_groups = groups_obj.get_most_relevant_results(search_string, 0)
    for entry in relevant_entries:
        entry.append('group')
        tok_k_results.append(entry)

    relevant_entries = media_obj.get_most_relevant_results(search_string, transitive_weight_from_groups, 0)
    for entry in relevant_entries:
        entry.append('media')
        tok_k_results.append(entry)

    tok_k_results.sort(key=itemgetter(1), reverse=True)

    return tok_k_results[0:num_results]


def get_objects_handler():
    file_location = 'sv_lsm_data.json'
    data = deserialize_data_from_disk(file_location)

    buildings = data['buildings']
    buildings_obj = Buildings(buildings)

    locks = data['locks']
    locks_obj = Locks(locks)

    groups = data['groups']
    groups_obj = Groups(groups)

    media = data['media']
    media_obj = Media(media)

    return buildings_obj, locks_obj, groups_obj, media_obj
