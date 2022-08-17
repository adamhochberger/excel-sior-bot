from typing import Dict, List

from utils.list_has_unique_values import list_has_unique_values


def generate_roles_for_player_dictionary(player_dictionary: Dict[str, str]) -> str:
    player_name_list = list(player_dictionary.values())
    player_name_list_is_unique = list_has_unique_values(player_name_list)

    if not player_name_list_is_unique:
        error_string = _get_unique_player_name_error_string(player_name_list)
        return error_string

    result_string = ""

    for player_number, player_name in player_dictionary.items():
        result_string += f"{player_number} - {player_name}\n"

    return result_string


def _get_unique_player_name_error_string(player_name_list: List[str]) -> str:
    duplicates_names = set([name for name in player_name_list if player_name_list.count(name) > 1])
    name_string = ", ".join(duplicates_names)

    result_string = \
        f"Error: There must be unique player names.\n" \
        f"Here is/are the name(s) occurring more than once: {name_string}"
