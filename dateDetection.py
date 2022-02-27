#regex that can detect dates in DD/MM/YYYY format
#dates range from 01-31
#months range from 01-12
#years range from 1000-2999
#ok to accept inconsistencies (leap years), write code to check for inconsistent days 
import re

#request user input
print('Enter a date in the format DD/MM/YYYY')
date = input()

#Step 1: Regex
dateRegex = re.compile(r'''
(0[1-9]|[1-2][0-9]|3[0-1])  #valid date can be 01-09, 10-29, 30-31
/                           #separator
(0[1-9]|1[0-2])             #valid month can be 01-09,10-12
/                           #separator
([1-2][0-9]{3})             #valid year can be 1000-2999
''', re.VERBOSE)


#Step 2: Store date into variables for year, month, and day 
dateSearch = dateRegex.search(date)
day, month, year = dateSearch.groups()


#Step 3: Check for inconsistent dates

#April, June, Sept, Nov have 30 days
if month == '04' or '06' or '09':
    if int(day) > 30:
        print('Invalid Date, these months only have 30 days')

if month == '02':
    if int(year) % 4 == 0:
        print('Year is divisible by 4')
        if int(year) % 400 == 0:
            print('400 year leap')
            if int(day) > 29:
                print('Invalid Date: This month only has 29 days')
        elif int(year) % 100 == 0:
            print('100 year leap, not 400 year leap')
            if int(day) > 28:
                print('Invalid Date: This month only has 28 days')
        else: 
            print('Regular leap year')
            if int(day) > 29:
                print('Invalid Date: This month only has 29 days')
    else: 
        print('Not a leap year')
        if int(day) > 28:
            print('Invalid Date: This month only has 28 days')

        
#February has 28 days unless leap year
#Leap year is when year is divisible by 4, unless evenly divisible by 100, unless also evenly divsible by 400 