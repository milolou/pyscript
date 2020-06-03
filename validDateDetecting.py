# validDateDetecting.py - Detecting dates in the DD/MM/YYYY formats,
# and check it.

import re,pyperclip

# Create the regex first.
dateRegex = re.compile(r'''(
   (0[1-9]|[1-2][0-9]|3[0-1])   #day
   /                            #separator
   (0[1-9]|1[0-2])              #month
   /                            #separator
   [1-2][0-9][0-9][0-9])        #year
   ''',re.VERBOSE)     

# To find matches.
match = []
text = str(pyperclip.paste())
for groups in dateRegex.findall(text):
    date = groups[0]
    match.append(date)

# Checking if the date is valid.
def validDates(List):
    for date in List:
        day = date[0:1]
        month = date[3:4]
        year = int(date[6:9])
        if (month == '04' or month == '06' or month == '09' or month == '11')\
           and day == '31':
            List.remove(date)
        if month == '02':
            if int(day) > 29:
                List.remove(date)
            if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
                List.remove(date)
    validDates = '\n'.join(List)
    print('Valid dates are copied to the clipboard.')
    pyperclip.copy('The valid dates are:\n' + validDates)
    print('The valid dates are:\n' + validDates)

# Run the program.
validDates(match)
            
        
            
