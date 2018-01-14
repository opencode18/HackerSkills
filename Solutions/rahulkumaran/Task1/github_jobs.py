import requests
import json
from bs4 import BeautifulSoup

jobDescription = raw_input("What technology do you want to work with? ")

jobLocation = raw_input("What's your preferred job location? ")

obj = requests.get("https://jobs.github.com/positions.json?description="+jobDescription+"&location="+jobLocation)

jsonObj = json.loads(obj.content)

suggestionNumber = 1
if(jsonObj):
	print "%d jobs have been found with the information you gave!"%len(jsonObj)
	for jobSearch in jsonObj:
		print ("------------------------------------------------------------")
		print ("Suggestion %d :"%suggestionNumber)
		print ("JOB TITLE	: " + jobSearch['title'])
		print ('\n')
		print ("COMPANY		: " + jobSearch['company'])
		print ('\n')
		print ("LOCATION	: " + jobSearch['location'])
		print ('\n')
		print ("TYPE		: " + jobSearch['type'])
		print ('\n')
		print ("COMPANY URL	: " + jobSearch['company_url'])
		print ('\n')
		descriptionSoup = BeautifulSoup(jobSearch['description'],'html.parser')
		print ("JOB DESCRIPTION : \n" + descriptionSoup.text)
		print ('\n')
		apply_soup = BeautifulSoup(jobSearch['how_to_apply'],'html.parser')
		print ("HOW TO APPLY?	: \n" + apply_soup.text)
		print ('\n')
		print ("------------------------------------------------------------")
		suggestionNumber+=1
		print ('\n\n')
else:
	print ("\n\nSorry but we have no jobs available currently with the preferences you entered.\nTry again soon! :)")



