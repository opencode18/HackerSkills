import re

inp_date = input()

date_month_format = r"\b(\d{2})\b"
year_format = r"(\d{4})"

match = re.findall(date_month_format, inp_date)

date = match[0]
month = match[1]

year_match = re.search(year_format, inp_date)
year = year_match.group()

out_date = month + '/' + date + '/' + year
print(out_date)