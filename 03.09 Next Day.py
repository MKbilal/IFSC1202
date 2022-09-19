#Prompt for a month (an integer from 1 to 12) and a day in the month (an integer from 1 to 31) in a common year (not a leap year).
#Print the month and the day of the next day after it.
#The first test corresponds to March 30 - next day is March 31
#The second test corresponds to March 31 - next day is April 1
#The third test corresponds to December 31 - next day is January 1

month = int(input("Enter month: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length = 31
elif month == 2:
        month_length = 28
else:
    month_length = 30

day = int(input("Enter day: "))

if day < month_length:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
    else:
        month += 1
print("Next day: %d/%d." % (month, day))
