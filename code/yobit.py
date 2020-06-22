#!env/Scripts/python
import requests

def get_price(element):
    url='https://yobit.net/api/2/{}_usd/ticker'.format(element)
    response=requests.get(url).json()
    price=response['ticker']['last']
    return '$' + str(price)

