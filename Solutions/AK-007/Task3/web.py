from urllib.request import urlopen
from bs4 import BeautifulSoup

web="https://scirate.com/"

page=urlopen(web)

soup=BeautifulSoup(page,"html.parser")

all_names=soup.find_all('div',attrs={'class' : 'title'})
all_links=soup.find_all('a',attrs={'title':'Download PDF'})
i=0
for name in all_names:
	print('Name = '+name.text)
	if(i<len(all_links)):
		print('Link = '+all_links[i]['href'])
	i=i+1
