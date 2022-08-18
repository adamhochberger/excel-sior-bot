import interactions


def get_list_of_options(number_of_options, names=[], description=[], types=[], required=[], choices=[]):
    option_list = []

    if type(names) != list:
        name_to_use = names

    if type(description) != list:
        description_to_use = description

    if type(types) != list:
        type_to_use = types

    if type(required) != list:
        required_value_to_use = required

    for num in range(0, number_of_options):
        if type(names) == list:
            name_to_use = names[num]

        if type(description) == list:
            description_to_use = description[num]

        if type(types) == list:
            type_to_use = types[num]

        if type(required) == list:
            required_value_to_use = required[num]

        option_list.append(
            interactions.Option(
                name=name_to_use,
                description=description_to_use,
                type=type_to_use,
                required=required_value_to_use,
                choices=choices
            )
        )

    return option_list
