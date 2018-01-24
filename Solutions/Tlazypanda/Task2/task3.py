import requests
from bs4 import BeautifulSoup

url = "https://scirate.com/"
site = requests.get(url)
scrape = BeautifulSoup(site.text,"lxml")


name = scrape.select('.title a')


link = scrape.select('a.paper-download')



for i in range(len(name)):
    
    print str(i+1)+". Name : "+name[i].getText()
    print '\n'
    print "Link : "+link[i].get('href')
    print '\n'