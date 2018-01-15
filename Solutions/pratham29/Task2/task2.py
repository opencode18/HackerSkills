import re
old_date=input()
new_date=re.sub(r'(\d{2})-(\d{2})-(\d{4})','\\2/\\1/\\3',old_date)
print(new_date)
