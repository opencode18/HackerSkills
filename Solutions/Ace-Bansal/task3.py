import bs4 as bs;
import requests;

source=requests.get('https://scirate.com/');
pageHTML=bs.BeautifulSoup(source.content,"html.parser");

articleTitle=pageHTML.find_all('div',class_='title');
articleLink=pageHTML.find_all('a',attrs={'title': "Download PDF"});

length=len(articleTitle);
for i in range(length):
    print(str(i+1)+")\n");
    print("ARTICLE TITLE:"+articleTitle[i].text);
    print("ARTICLE LINK:"+articleLink[i].get('href'));
    print("\n");
    print("=============================================================================\n");
