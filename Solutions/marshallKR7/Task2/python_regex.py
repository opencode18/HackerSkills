#Importing regex module
import re
#Taking Date as input 
Input_Date = input()
Date_Month = r"\b(\d{2})\b"
Year = r"(\d{4})"
Match = re.findall(Date_Month, Input_Date)
Date = Match[0]
Month = Match[1]
Year = re.search(Year, Input_Date)
Year = Year.group()
#Combining month,date and year in Output_Date
Output_Date = Month+'/'+Date+'/'+Year
#printing final date in MM/DD/YY format
print(Output_Date)
