import random
from copy import deepcopy
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

    role_list = deepcopy(ROLE_NAME_LIST)
    random.shuffle(role_list)

    result_string = get_role_probability_string(role_order=role_list, player_name_list=player_name_list)

    return result_string


def _get_unique_player_name_error_string(player_name_list: List[str]) -> str:
    duplicates_names = set([name for name in player_name_list if player_name_list.count(name) > 1])
    name_string = ", ".join(duplicates_names)

    result_string = \
        f"Error: There must be unique player names.\n" \
        f"Here is/are the name(s) occurring more than once: {name_string}"

    return result_string


def get_role_probability_string(role_order: List[str], player_name_list: List[str]) -> str:
    players_that_need_roles = set(player_name_list)

    result_message = ""

    for role in role_order:
        preferred_players = []
        neutral_players = []
        non_preferred_players = []

        for player_name in players_that_need_roles:
            if role == PLAYER_PREFERENCE_DICTIONARY[player_name]["preferred"]:
                preferred_players.append(player_name)
            elif role == PLAYER_PREFERENCE_DICTIONARY[player_name]["non_preferred"]:
                non_preferred_players.append(player_name)
            else:
                neutral_players.append(player_name)

        preferred_player_count = len(preferred_players)
        neutral_player_count = len(neutral_players)
        non_preferred_player_count = len(non_preferred_players)

        total_probability_score = PREFERRED_WEIGHT * preferred_player_count + NEUTRAL_WEIGHT * neutral_player_count + \
            NON_PREFERRED_WEIGHT * non_preferred_player_count

        preferred_probability = PREFERRED_WEIGHT / total_probability_score
        neutral_probability = NEUTRAL_WEIGHT / total_probability_score
        non_preferred_probability = NON_PREFERRED_WEIGHT / total_probability_score

        print(role)
        name_list = preferred_players + neutral_players + non_preferred_players
        print(name_list)
        probability_list = [preferred_probability] * preferred_player_count + \
                           [neutral_probability] * neutral_player_count + \
                           [non_preferred_probability] * non_preferred_player_count

        print(probability_list)

        random_player = random.choices(name_list, weights=probability_list, k=1)[0]
        result_message += f"{random_player} - {role}\n"

        players_that_need_roles.remove(random_player)

    return result_message
