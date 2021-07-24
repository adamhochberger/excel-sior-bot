import csv
from tabulate import tabulate
from os import read

class UniteParser():

    def __init__(self, item):
        self.INFO_LIST =  ['Levels', 'Enhancers', 'Dollars / Level']
        self.ITEMS_LIST = ['Muscle Band', 'Scope Lens', 'Shell Bell', 'WiseGlasses', 'Focus Band', 'Energy Amplifier', 'Float Stone', 'Buddy Barrier', 'Score Shield', 'Aeos Cookie', 'Attack Weight', 'Sp Atk Specs', 'Leftovers', 'Assault Vest', 'Rocky Helmet']

        self.item_to_print = item

    def csv_parse(self):
        pass
    
if __name__ == "__main__":
    UniteParser("WiseGlasses").csv_parse()