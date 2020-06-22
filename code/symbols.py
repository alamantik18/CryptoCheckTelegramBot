import requests
from bs4 import BeautifulSoup

URL = 'https://coinmarketcap.com/all/views/all/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('td', class_='cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__symbol')
    symbols = []
    for item in items:
        symbols.append(
           item.find('div').get_text(),
        )
    return symbols


def parse():
    html = get_html(URL)
    symbols = get_content(html.text)
    return symbols


