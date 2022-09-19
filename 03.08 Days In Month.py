#Given a month - an integer from 1 (January) to 12 (December), print the number of days in the month.
#Assume that it is a non-leap year.


month = int(input("Enter month: "))

if month in [9, 4, 6, 11]:
    print (30)

elif month in [1, 3, 5, 7, 8, 10, 12]:
    print (31) 
else:
    print(28)
