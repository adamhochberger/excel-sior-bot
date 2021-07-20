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

    def parse_anchors(self):

        # Retrieve all of the anchor tags
        tags = self.the_soup.find_all('a')
        for tag in tags:
            print(tag.get('href', None))

    def parse_ability(self):
        pass

    def parse_stats(self):
        pass

    def parse_item(self):
        pass


def main():
    url = "https://leagueoflegends.fandom.com/wiki/Annie/LoL"
    url_parser = Parser(url)
    url_parser.parse_anchors()


if __name__ == "__main__":
    main()
