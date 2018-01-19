from bs4 import BeautifulSoup
import requests
import re


r  = requests.get("https://scirate.com/")

html_page = r.text


soup = BeautifulSoup(html_page,"lxml")
links = []

 
for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
    links.append(link.get('href'))


solved = soup.find_all('div', class_='title')
for i in range (len(solved)):
	print("News Title and Pdf Download Link:" )
	print(solved[i].string)
	print(links[i])