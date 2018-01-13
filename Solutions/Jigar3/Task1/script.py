import requests, json
from bs4 import BeautifulSoup

print("Enter Job Description")
jobDes = raw_input()

print("Enter the Location")
location = raw_input()

obj = requests.get("https://jobs.github.com/positions.json?description="+jobDes+"&location="+location)

jsonObj = json.loads(obj.content)

if (jsonObj):
    j=1
    for i in jsonObj:
        print("Job " + str(j) + " ==>\n")
        print("Title: " + i['title'] + "\n")
        print("Location: " + i['location'] + "\n")
        print("Type: " + i["type"] + "\n")
        soup1 = BeautifulSoup(i['description'], "lxml")
        print("Description: " + soup1.get_text() + "\n")
        soup2 = BeautifulSoup(i['how_to_apply'], "lxml")
        print("How to Apply: " + soup2.get_text() + "\n")
        print("Company: " + i["company"] + "\n")
        print("Company Website: " + i["company_url"] + "\n")
        j+=1
        print("---------------------------------------------------------------------")
else:
    print("No Jobs Found")
