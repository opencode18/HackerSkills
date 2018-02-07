import re;

userDate=input("Enter the date. Please use 'DD-MM-YYYY' format\n");
rObj= re.compile(r'(\d\d)-(\d\d)-(\d\d\d\d)');
ddmmyyyy = rObj.search(userDate);

print("The date in new format is:");
print(ddmmyyyy.group(2)+"-"+ddmmyyyy.group(1)+"-"+ddmmyyyy.group(3));
