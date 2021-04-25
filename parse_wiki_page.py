# parse_wiki_page.py
import requests
from bs4 import BeautifulSoup


def parse_anchors(url):    
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup.find_all('a')
    for tag in tags:
        print(tag.get('href', None)) 


def main():
    url = "https://leagueoflegends.fandom.com/wiki/Annie/LoL"
    parse_anchors(url)


if __name__ == "__main__":
    main()