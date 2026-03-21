# datetime: 
#       In Python, the datetime module is the standard library for manipulating dates and times. 
#       It provides classes to handle date and time arithmetic, formatting, and time zone information

from datetime import datetime, timedelta

# Getting Current Date and Time
now = datetime.now()
print(now)

# Getting Only the Date
# from datetime import date
# today = date.today()    
# print(today)


# Formatting Dates
now = datetime.now()
formatted = now.strftime("%d/%m/%Y %H:%M:%S")
print(formatted)

formatted_2 = now.strftime("%A, %d-%m-%Y")
print(formatted_2)