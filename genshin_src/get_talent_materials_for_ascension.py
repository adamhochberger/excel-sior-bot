from .constants import ASCENSION_MATERIALS_PER_LEVEL_DICTIONARY_LIST, GREEN_TO_BLUE_BOOK_MULTIPLIER, GREEN_TO_PURPLE_BOOK_MULTIPLIER
    

def get_talent_materials_for_ascension(current_talent_level: int, target_talent_level: int) -> str:
    if target_talent_level <= current_talent_level:
        return f"The target talent level ({target_talent_level}) needs to be greater than the current target level {current_talent_level}."

    list_of_ascensions = ASCENSION_MATERIALS_PER_LEVEL_DICTIONARY_LIST[current_talent_level-1:target_talent_level-1]

    stat_dictionary = {
        'mora': 0, 'character_material': {'white': 0, 'green': 0, 'blue': 0}, 'book': {'green': 0, 'blue': 0, 'purple': 0}, 'boss_material': 0, 'crown': 0
    }

    for ascension_dictionary in list_of_ascensions:
        for key, value in ascension_dictionary.items():
            if type(value) == tuple:
                substat_type = value[0]
                stat_dictionary[key][substat_type] += value[1]
            else: 
                stat_dictionary[key] += ascension_dictionary[key]

    green_book_equivalent = get_green_book_equivalent(stat_dictionary['book'])
    minimum_domain_runs = round(green_book_equivalent / 8)

    message_string = \
        f"```" + \
        f"GBE: {get_green_book_equivalent(stat_dictionary['book'])}\n" + \
        f"Required materials from talent level {current_talent_level} to {target_talent_level}\n" + \
        f"Maximum number of 20 resin domain runs for talents (assuming 2/2/0 and no Xingqiu): {minimum_domain_runs}\n" + \
        f"Resin required: {minimum_domain_runs*20}\n" + \
        f"\n" + \
        f"Mora: {stat_dictionary['mora']}\n" + \
        f"Character Materials:\n" + \
            f"    White: {stat_dictionary['character_material']['white']}\n" + \
            f"    Green: {stat_dictionary['character_material']['green']}\n" + \
            f"    Blue: {stat_dictionary['character_material']['blue']}\n" + \
        f"Talent Books:\n" + \
            f"    Green: {stat_dictionary['book']['green']}\n" + \
            f"    Blue: {stat_dictionary['book']['blue']}\n" + \
            f"    Purple: {stat_dictionary['book']['purple']}\n" + \
        f"Boss Materials: {stat_dictionary['boss_material']}\n" + \
        f"Crowns: {stat_dictionary['crown']}\n" + \
        f"```"

    return message_string


def get_green_book_equivalent(book_dictionary: dict) -> int:
    return book_dictionary['green'] + book_dictionary['blue'] * GREEN_TO_BLUE_BOOK_MULTIPLIER + book_dictionary['purple'] * GREEN_TO_PURPLE_BOOK_MULTIPLIER