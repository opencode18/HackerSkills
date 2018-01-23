import re
def new_date_format(date):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', date)
newdate = "2017-01-19"
print("New Date format",new_date_format(newdate))
