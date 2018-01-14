from bs4 import BeautifulSoup
import requests

document = requests.get("https://scirate.com/")
soup = BeautifulSoup(document.content, "html.parser")

titles = soup.select(".title a")
links = soup.find_all("a", attrs={'title': "Download PDF"})
i=0
for title in titles:
    print("Title: " + title.text)
    if(i<len(links)):
        print("Link: " + links[i]['href'])
    print("---------------------------------------------------------------------")
    i+=1
