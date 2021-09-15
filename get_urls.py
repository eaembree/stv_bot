import json
from bs4 import BeautifulSoup
from get_page import get_page


def get_new_item_urls():
    html = get_page('http://www.storytellersvault.com')
    soup = BeautifulSoup(html, 'html.parser')

    all_links = soup.find_all('a', href=True)
    all_links = list(all_links)
    new_products = [
        x for x in all_links if "?src=newest_community" in x.get('href')][::2]

    urls = [x.get('href') for x in new_products]
    urls = [x.split("?")[0] for x in urls]

    with open('tmp.json', 'r') as filename:
        most_recent = json.load(filename)['most_recent']
    new_items = urls[:urls.index(most_recent)]
    return new_items
