import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.findAll('a')
new_list = []
for link in links:
    if link.text.startswith(letter) and len(link.text) > 1:
        if 'topics' in link.get('href') or 'entity' in link.get('href'):
            new_list.append(link.text)
print(new_list)
