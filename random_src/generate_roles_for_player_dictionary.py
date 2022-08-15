from typing import Dict


def generate_roles_for_player_dictionary(player_dictionary: Dict[str, str]) -> str:
    result_string = ""

    player_name_list = list(player_dictionary.values())

    if len(player_name_list) > len(set(player_name_list)):
        duplicates_names = set([name for name in player_name_list if player_name_list.count(name) > 1])
        name_string = ", ".join(duplicates_names)

        result_string = \
            f"Error: There must be unique player names.\n" \
            f"Here is/are the name(s) occurring more than once: {name_string}"
        return result_string

    for player_number, player_name in player_dictionary.items():
        result_string += f"{player_number} - {player_name}\n"

    return result_string
