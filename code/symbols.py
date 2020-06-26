import requests
from bs4 import BeautifulSoup


URL = 'https://coinmarketcap.com/all/views/all/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr', class_='cmc-table-row')
    symbols = []
    price = []
    for item in items:
        symbols.extend([
                item.find('a', class_='cmc-link').get_text(),
                item.find('td', class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__symbol").get_text(),
            ])
        # price.append(
        #     item.find('td', class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price").get_text()
        # )
    return symbols

def get_price(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr', class_='cmc-table-row')
    price = []
    for item in items:
        price.append(
            item.find('td', class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price").get_text()
        )
    return price

def get_hour(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr', class_="cmc-table-row")
    hour = []
    for item in items:
        hour.append(
            item.find('td', class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-1-h").get_text()
        )
    return hour

def get_day(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr', class_="cmc-table-row")
    day = []
    for item in items:
        day.append(
            item.find('td', class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h").get_text(),
        )
    return day

def get_week(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr', class_="cmc-table-row")
    week = []
    for item in items:
        week.append(
            item.find('td', class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-7-d").get_text()
        )
    return week

def parse():
    html = get_html(URL)
    symbols = get_content(html.text)
    price = get_price(html.text)
    hour = get_hour(html.text)
    day = get_day(html.text)
    week = get_week(html.text)
    return symbols, price, hour, day, week