#Prompt for a 4 digit year'
#If the year is a leap year, print "LEAP YEAR", otherwise print "COMMON YEAR".
#The rules in Gregorian calendar are as follows:
#A year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
#A year is always a leap year if its number is exactly divisible by 400

n = int(input("Enter year: "))
if n % 400 == 0 or n % 100 != 0 and n % 4 == 0:
  print("LEAP YEAR")
else:
    print("COMMON YEAR")

