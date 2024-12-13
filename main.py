"""
Written by: Denis Chechulin
Date: Sep 26, 2024
"""

#the year to check
year = int(2023)

notLeapYear = "there are 365 days"
leapYear = "there are 366 days"

#check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(leapYear)
else:
    print(notLeapYear)