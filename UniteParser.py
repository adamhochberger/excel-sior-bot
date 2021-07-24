import csv
from tabulate import tabulate

ITEMS_LIST = ['Muscle Band', 'Scope Lens', 'Shell Bell', 'Wise Glasses', 'Focus Band', 'Energy Amplifier', 'Float Stone', 'Buddy Barrier', 'Score Shield', 'Aeos Cookie', 'Attack Weight', 'Sp Atk Specs', 'Leftovers', 'Assault Vest', 'Rocky Helmet']
INFO_LIST =  ['Levels', 'Enhancers', 'Dollars / Level']

class UniteParser():
    
    def __init__(self, item, ):
        #[print(item) for item in (Items)]
        self.CONSTANTS_LIST = INFO_LIST + [item]
        self.item_dictionary = {key: {} for key in self.CONSTANTS_LIST}
        self.item_to_print = item

    def parse_csv(self, filename):    
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file)
            big_list = []
            for row in reader:
                big_list.append(row)

        return zip(*big_list)

    def read_description_from_csv(self):
        transposed_csv = self.parse_csv("description_sheet.csv")
        for row in transposed_csv:
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
        transposed_csv = self.parse_csv("stat_sheet.csv")
        for row in transposed_csv:
            key_string = row[0]
        
            for constant in self.CONSTANTS_LIST:
                if key_string.find(constant) >= 0:
                    key_string = key_string.replace(constant + " ", "")
                    self.item_dictionary[constant][key_string] = row[1:]
        
        constants_with_item = {key: self.item_dictionary[key][key] for key in INFO_LIST}
        for key, value in self.item_dictionary[self.item_to_print].items():
            constants_with_item[key] = value

        item_table_string = self.item_to_print + "\n" + tabulate(constants_with_item, headers="keys", tablefmt="pretty")
        # print(item_table_string)
        return item_table_string

if __name__ == "__main__":
    UniteParser(None)