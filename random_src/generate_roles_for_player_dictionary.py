import random
from typing import Dict, List

from utils.list_has_unique_values import list_has_unique_values

PREFERRED_WEIGHT = 6
NEUTRAL_WEIGHT = 2
NON_PREFERRED_WEIGHT = 1

ROLE_NAME_LIST = ["ASSASSIN", "GUARDIAN", "HUNTER", "MAGE", "WARRIOR"]

PLAYER_PREFERENCE_DICTIONARY = {
    "Adam": {
        "preferred": "GUARDIAN",
        "non_preferred": "ASSASSIN"
    },
    "Annan": {
        "preferred": "MAGE",
        "non_preferred": ""
    },
    "Brady": {
        "preferred": "ASSASSIN",
        "non_preferred": "HUNTER"
    },
    "Giancarlo": {
        "preferred": "HUNTER",
        "non_preferred": "ASSASSIN"
    },
    "Jonathan": {
        "preferred": "",
        "non_preferred": "ASSASSIN"
    },
    "Michael": {
        "preferred": "HUNTER",
        "non_preferred": "WARRIOR"
    }

}


def generate_roles_for_player_dictionary(player_dictionary: Dict[str, str]) -> str:
    player_name_list = list(player_dictionary.values())
    player_name_list_is_unique = list_has_unique_values(player_name_list)

    if not player_name_list_is_unique:
        error_string = _get_unique_player_name_error_string(player_name_list)
        return error_string

    random.shuffle(player_name_list)
    random.shuffle(ROLE_NAME_LIST)

    result_string = ""

    for player, role in zip(player_name_list, ROLE_NAME_LIST):
        result_string += f"{player} - {role}\n"

    return result_string


def _get_unique_player_name_error_string(player_name_list: List[str]) -> str:
    duplicates_names = set([name for name in player_name_list if player_name_list.count(name) > 1])
    name_string = ", ".join(duplicates_names)

    result_string = \
        f"Error: There must be unique player names.\n" \
        f"Here is/are the name(s) occurring more than once: {name_string}"
