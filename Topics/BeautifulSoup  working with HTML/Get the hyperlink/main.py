import requests

from bs4 import BeautifulSoup
num_act = int(input())
page_link = input()
r = requests.get(page_link)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.findAll("a", href=f"#act{num_act}")[0].get('href'))
