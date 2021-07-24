import csv
from tabulate import tabulate
from os import read

ITEMS_LIST = ['Muscle Band', 'Scope Lens', 'Shell Bell', 'WiseGlasses', 'Focus Band', 'Energy Amplifier', 'Float Stone', 'Buddy Barrier', 'Score Shield', 'Aeos Cookie', 'Attack Weight', 'Sp Atk Specs', 'Leftovers', 'Assault Vest', 'Rocky Helmet']
INFO_LIST =  ['Levels', 'Enhancers', 'Dollars / Level']

class UniteParser():
    
    def __init__(self, item):
        self.CONSTANTS_LIST = INFO_LIST + [item]
        self.item_dictionary = {key: {} for key in self.CONSTANTS_LIST}
        self.item_to_print = item

    def csv_parse(self):    
        with open('stat_sheet.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            big_list = []
            for row in reader:
                big_list.append(row)

        transposed_csv = zip(*big_list)
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
    UniteParser("WiseGlasses").csv_parse()