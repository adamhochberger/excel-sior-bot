from typing import List


def list_has_unique_values(player_name_list: List[str]) -> bool:
    number_of_values_in_list = len(player_name_list)
    number_of_values_in_set = len(set(player_name_list))

    if number_of_values_in_list > number_of_values_in_set:
        return False

    return True
