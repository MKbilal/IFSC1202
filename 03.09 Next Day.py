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