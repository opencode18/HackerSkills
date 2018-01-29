from bs4 import BeautifulSoup as bs
import requests, json

print("Enter the location of the job")
loc = raw_input()
print("Enter your job description")
job_des = raw_input()
source = requests.get("https://jobs.github.com/positions.json?description="+job_des+"&location="+loc)
jsonObj = json.loads(source.content)

i = 1
if (jsonObj):
    print("\n\nJOBS FOUND!!\n\n")
    for j in jsonObj:
        print("-----------------------------------" + str(i) + "---------------------------------\n\n")
        print("TITLE: " + j['title'] + "\n\n")
        print("COMPANY: " + j["company"] + "\n")
        print("LOCATION: " + j['location'] + "\n\n")
        print("TYPE: " + j["type"] + "\n\n")
        desc = bs(j['description'], "lxml")
        print("DESCRIPTION: " + desc.get_text() + "\n\n")
        hta = bs(j['how_to_apply'], "lxml")
        print("PLEASE CHECK: " + hta.get_text() + "\n\n")
        print("WEBSITE: " + j["company_url"] + "\n\n")
        print("------------------------------- X --------------------------------------\n\n\n")
        i += 1
else:
    print("------------------SORRY NO JOBS FOUND!---------------")
