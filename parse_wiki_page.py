# parse_wiki_page.py
from gazpacho import get, Soup

class Parser:

    def __init__(self, url):
        self.the_soup = None
        self.make_the_soup(url)

    def make_the_soup(self, url):
        html = get(url)
        self.the_soup = Soup(html)

    def remake_the_soup(self, url):
        self.make_the_soup(url)

    def parse_ability(self):
        # Retrieve all of the ability divs
        ability_div_tags = self.the_soup.find('div', {"class": "ability-info-container"}, partial=False, mode="all")

        for ability_div_tag in ability_div_tags:
            first_h3_tag_text = ability_div_tag.find('h3', mode="first").text
            print(first_h3_tag_text)


    def parse_stats(self):
        pass

    def parse_item(self):
        pass

def main():
    url = "https://leagueoflegends.fandom.com/wiki/Annie/LoL"
    url_parser = Parser(url)
    url_parser.parse_ability()


if __name__ == "__main__":
    main()
