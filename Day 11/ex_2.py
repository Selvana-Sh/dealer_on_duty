# calculate number of days between two dates

from datetime import date

def num_of_days(date1, date2):
    return (date2-date1).days

year1 = int(input("Enter first date's year: "))
month1 = int(input("Enter first date's month: "))
day1= int(input("Enter first date's day: "))

year2 = int(input("Enter last date's year: "))
month2 = int(input("Enter last date's month: "))
day2= int(input("Enter last date's day: "))

fist_date = date(year1, month1, day1)
last_date = date(year2, month2, day2)

print(f'{num_of_days(fist_date, last_date)} days')