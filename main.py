from bs4 import BeautifulSoup
import requests

home = 'https://fr.wikipedia.org'

html_text = requests.get(home).text
soup = BeautifulSoup(html_text, 'lxml')
for a in soup.find_all('a', href=True):
    if a['href'][0] == '/' and a['href'][1] == 'w':
        print(home + a['href'])