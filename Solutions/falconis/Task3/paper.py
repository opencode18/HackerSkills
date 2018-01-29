import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://scirate.com/').read()
page = bs.BeautifulSoup(source, 'lxml')

names = page.find_all('div', class_='title')
links = page.find_all('a', class_ = 'paper-download btn btn-success')
num = len(names)
for x in range(num):
    print("--------------------------------" + str(x+1) + "---------------------------------")
    print("TITLE:" + names[x].text)
    print("LINK:" + links[x].get('href'), end='\n\n')
    