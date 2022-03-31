#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

def request():
    url = "https://status.ix.br"
    return requests.get(url)

def parse_result(html):
    bs = BeautifulSoup(html, 'html.parser')
    ixlist = bs.find_all('ul', {'class': 'list-group components'})

    data = {}
    print("[")
    for ix in ixlist:
            name = ix.find('strong').text.strip()
            items = ix.find('div', {'class': 'group-items'}).find_all('li', {'class': 'list-group-item'})
            ix_data = {}
            for item in items:
                status_div = item.find('div', {'class': 'pull-right'})
                status = status_div.text.strip()
                status_div.decompose()
                item_name = item.text.strip()
                print("\t")
                print("\t{\n")
                print(f'\t\t"{"{#IX}"}": "{name}",')
                print(f'\t\t"{"{#IX2}"}": "{item_name}",')
                print(f'\t\t"{"{#STATUS}"}": "{status}"')
                print("\t},\n")
    return data

if __name__ == '__main__':
    response = request()

print(parse_result(response.text))

print("]")
