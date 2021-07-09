from bs4 import BeautifulSoup
import requests

home = 'https://fr.wikipedia.org'
all_link = ['']
for i in range(50):
    html_text = requests.get(home + all_link[i]).text
    soup = BeautifulSoup(html_text, "lxml")
    for a in soup.find_all('a', href=True):
        if a['href'][0] == '/' and a['href'][1] == 'w' and a['href'][2] == 'i':
            find = False
            for link in all_link:
                if link == a['href']:
                    find = True
                    break
            if not find:
                all_link.append(a['href'])
    print('[{}]'.format(i), len(all_link))
print(len(all_link))