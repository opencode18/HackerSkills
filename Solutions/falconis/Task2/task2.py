import re

inp = input()
reg = r'\d\d\-\d\d\-\d\d\d\d'
mth = re.search(reg,inp)
str = mth.group()
ans = str[3:5]+'/'+str[:2]+'/'+str[6:]
print(ans)