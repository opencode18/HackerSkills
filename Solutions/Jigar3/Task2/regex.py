import re

date = raw_input("Enter the date in DD-MM-YYYY format\n")
regex = re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)')
rGroups = regex.search(date)

print("Converted the date in MM/DD/YYYY format->")
print(rGroups.group(2)+"/"+rGroups.group(1)+"/"+rGroups.group(3))
