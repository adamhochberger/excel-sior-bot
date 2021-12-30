import csv
from tabulate import tabulate
from UniteEnum import UniteInformation, UniteItems

class UniteParser():
    
    def __init__(self, item):
        self.COLUMN_LIST = [UniteInformation.LEVELS.value, item]
        self.item_dictionary = {}
        self.item_to_print = item

    def parse_csv(self, filename):    
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            csv_as_list = []
            for row in reader:
                if row[0] == UniteInformation.LEVELS.value or self.item_to_print in row[0]:
                    csv_as_list.append(row)

            return csv_as_list

    def read_description_from_csv(self):
        csv_as_list = self.parse_csv("unite_csv/description_sheet.csv")
        for row in csv_as_list:
            key_string = row[0]

            if self.item_to_print in key_string:
                base_description_string = row[1]
                rank1_value = row[2]
                rank2_value = row[3]
                rank3_value = row[4]

                description_string =  f"{self.item_to_print}\n" + \
                    f"Levels 1-9: {base_description_string.format(value=rank1_value)}\n" + \
                    f"Levels 10-19: {base_description_string.format(value=rank2_value)}\n" + \
                    f"Levels 20-30: {base_description_string.format(value=rank3_value)}\n"

                return description_string

    def read_stats_from_csv(self):
        csv_as_list = self.parse_csv("unite_csv/stat_sheet.csv")
        for row in csv_as_list:
            key_string = row[0]

            if key_string == UniteInformation.LEVELS.value or self.item_to_print in key_string:
                key_string = key_string.replace(self.item_to_print + " ", "")
                self.item_dictionary[key_string] = row[1:]

        item_table_string = tabulate(self.item_dictionary, headers="keys", tablefmt="pretty")
        return item_table_string

# if __name__ == "__main__":
    
#     print(UniteParser(UniteItems.SCOPE_LENS.value).read_description_from_csv())
#     print(UniteParser(UniteItems.SCOPE_LENS.value).read_stats_from_csv())