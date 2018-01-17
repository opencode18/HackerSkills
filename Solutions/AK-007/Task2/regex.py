import re

user_input=input()
date=re.sub(r'(\d{2})-(\d{2})-(\d{4})','\\2/\\1/\\3',user_input)

print('Converted format : '+ date)