from typing import List

from pokemon_unite_src.UniteParser import UniteParser
from utility_functions import split_string, convert_string_to_codeblock_string


def get_unite_item_table_string_list(item_name: str, should_codeblock_format_string: bool) -> List[str]:
    # Initialize parser and read the blocks of data for the item
    unite_parser = UniteParser(item_name)
    table_string = unite_parser.read_description_from_csv()
    table_string += unite_parser.read_stats_from_csv()

    # Split the string in case it exceeds the message character limit
    message_string_list = []

    for section in split_string(table_string):
        string_to_append = convert_string_to_codeblock_string(section) if should_codeblock_format_string else section
        message_string_list.append(string_to_append)

    return message_string_list
