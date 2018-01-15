from bs4 import BeautifulSoup
import mechanize

browser = mechanize.Browser()
reponse = browser.open("https://scirate.com/")
soup = BeautifulSoup(reponse,'html.parser')

name_list = soup.find_all('div',attrs={'class':'title'})
link_list = soup.find_all('a',attrs={'title':'Download PDF'})

i = 0

for topics in name_list:
	print str(i+1)+') '+topics.text
	print link_list[i].get('href')
	i+=1
	print"----------------------------------------------------------------------"

