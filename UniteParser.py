import csv
from tabulate import tabulate
from os import read

class UniteParser():

    def __init__(self, item):
        self.INFO_LIST =  ['Levels', 'Enhancers', 'Dollars / Level']
        self.ITEMS_LIST = ['Muscle Band', 'Scope Lens', 'Shell Bell', 'WiseGlasses', 'Focus Band', 'Energy Amplifier', 'Float Stone', 'Buddy Barrier', 'Score Shield', 'Aeos Cookie', 'Attack Weight', 'Sp Atk Specs', 'Leftovers', 'Assault Vest', 'Rocky Helmet']

        self.item_to_print = item

    def csv_parse(self):
        with open('stat_sheet.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            big_list = []
            for row in reader:
                big_list.append(row)

        transposed_csv = zip(*big_list)
if __name__ == "__main__":
    UniteParser("WiseGlasses").csv_parse()