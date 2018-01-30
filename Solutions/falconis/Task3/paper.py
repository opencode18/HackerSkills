import bs4 as bs
import requests

source = requests.get('https://scirate.com/')
page = bs.BeautifulSoup(source.text, 'lxml')

names = page.find_all('div', class_='title')
links = page.find_all('a', class_ = 'paper-download btn btn-success')
num = len(names)
for x in range(num):
    print("--------------------------------" + str(x+1) + "---------------------------------")
    print("TITLE:" + names[x].text)
    print("LINK:" + links[x].get('href'), end='\n\n')
    