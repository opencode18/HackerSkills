import re

date =str(input())
dateregex = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')
verify = dateregex.search(date)
if(verify==None):
	print("Date input form not Valid")
else:
	print(verify.group(2)+"/"+verify.group(1)+"/"+verify.group(3))