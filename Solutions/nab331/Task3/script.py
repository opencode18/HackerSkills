import urllib2
from bs4 import BeautifulSoup
#import webbrowser


wiki = "https://scirate.com/"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page,"html.parser")

all_links = soup.find_all("div",{"class": "title"})

for link in all_links:
	print link.string
	for i in link:
		pdf_link = "http://arxiv.org/pdf/"+i['href'].split("/")[2]+".pdf"
		#webbrowser.open(pdf_link)
	print
