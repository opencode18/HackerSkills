import re

exp= input()
date = r'(\d{2})-(\d{2})-(\d{4})'
reg = re.search(date,exp)
str = reg.group()
month=str[3:5]
day=str[:2]
year=str[6:]
ans = month+'-'+day+'-'+year
print(ans)