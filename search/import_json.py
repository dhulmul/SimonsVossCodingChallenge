import json

from search.buildings import Buildings
from search.groups import Groups
from search.locks import Locks
from search.media import Media


def deserialize_data_from_disk(json_location):
    file_mode = 'r'
    with open(json_location, file_mode) as read_file:
        data = json.load(read_file)

        buildings = data['buildings']
        buildings_obj = Buildings(buildings)

        locks = data['locks']
        locks_obj = Locks(locks)

        groups = data['groups']
        groups_obj = Groups(groups)

        media = data['media']
        media_obj = Media(media)

        # print(buildings_obj.get_all_buildings())
        # print(locks_obj.get_all_locks())
        # print(groups_obj.get_all_groups())
        # print(media_obj.get_all_media())
        # for r in buildings_obj.get_most_relevant_results('HOFF', 50):
        #     print(r)

        for r in groups_obj.get_most_relevant_results('Vorstand', 50):
            print(r)

deserialize_data_from_disk('../sv_lsm_data.json')