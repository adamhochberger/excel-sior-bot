# parse_wiki_page.py
import requests
from bs4 import BeautifulSoup


class Parser:
    the_soup = None

    def __init__(self, url):
        self.make_the_soup(url)

    def make_the_soup(self, url):
        resp = requests.get(url)
        soup = BeautifulSoup(resp.content, 'html.parser')

        self.the_soup = soup

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
