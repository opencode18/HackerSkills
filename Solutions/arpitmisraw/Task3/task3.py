import requests
from bs4 import BeautifulSoup

url = "https://scirate.com/"
resp = requests.get(url)

html = resp.text
scirate_soup = BeautifulSoup(html)


title = scirate_soup.select('.title a')


href = scirate_soup.select('a.paper-download')



for i in range(len(title)):
    print(i+1,". ",title[i].getText(),'\n','Link:',href[i].get('href'),'\n\n')
