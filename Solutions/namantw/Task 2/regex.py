#python 2.7
import re

date = raw_input()
print "" + re.sub(r'(\d{1,2})-(\d{1,2})-(\d{4})', '\\2/\\1/\\3', date)