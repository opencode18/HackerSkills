import re
def change_date_format(dt):
        return re.sub(r'(\d{1,2})-(\d{1,2})-(\d{4})', '\\2/\\1/\\3', dt)
dt1 = input()
print("date in DD-MM-YYYY Format: ",dt1)
print("date in MM-DD-YYYY Format: ",change_date_format(dt1))
