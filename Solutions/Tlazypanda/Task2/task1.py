import requests, json
from bs4 import BeautifulSoup

print("Enter Job Description")
jd = raw_input()

print("Enter the Location")
loc = raw_input()
link="https://jobs.github.com/positions.json?description="+jd+"&location="+loc
jobobj = requests.get(link)

object = json.loads(jobobj.text)

if (object):
    j=1
    for i in object:
        print("Job " + str(j) + " ==>\n")
        print("Title: " + i['title'] + "\n")
        print("Date added: " + i['created_at'] + "\n")
        print("Location: " + i['location'] + "\n")
        print("Type: " + i["type"] + "\n")
        s1 = BeautifulSoup(i['description'], "lxml")
        print("Description: " + soup1.getText() + "\n")
        print("Company: " + i["company"] + "\n")
        print("Company Website: " + i["company_url"] + "\n")
        j+=1
else:
    print("No Jobs Found")