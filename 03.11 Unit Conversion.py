#Create a python program that performs unit conversions. You code should do the following:

#Prompt for a floating point number (FromValue). Your prompt should display "Enter From Value: "
#Prompt for the unit to convert from (FromUnit). Your prompt should display "Enter From Unit (in, ft, yd, mi):"
#Using an if statement make sure that the from unit is one of the following: in, ft, yd, mi. If not, display "FromUnit is not valid" and then exit the program
#Prompt for the unit to convert to (ToUnit). Your prompt should display "Enter From Unit (in, ft, yd, mi):"
#Using an if statement make sure that the to unit is one of the following: in, ft, yd, mi. If not, display "ToUnit is not valid" and then exit the program
#Using a series of if statements, determine the value of multiplier needed to convert the value using the FromUnit to the ToUnit. You will need 16 of them. If a user enters the same FromUnit and ToUnit, then the multiplier is 1.0 (See http://www.unit-conversion.info/length.html)
#if FromUnit == "ft" and ToUnit == "yd": multiplier = 0.3333333333

#Finally, multiply the multiplier times the FromValue to get the ToValue (Use the round function to round to 7 digits)
#Display the FromValue, FromUnit, ToValue and ToUnit as shown
#Here are some test cases. You answer may be slightly different due to rounding.






FromValue = float(input("Enter From Value: "))
FromUnit = input("Enter From Unit (in, ft, yd, mi): ")

if FromUnit != "in" and FromUnit != "ft" and FromUnit != "yd" and FromUnit !="mi":   
    print("FromUnit is not valid")
    exit()

ToUnit = input("Enter To Unit (in, ft, yd, mi): ")
if ToUnit != "in" and ToUnit != "ft" and ToUnit != "yd" and ToUnit !="mi":
    print("ToUnit is not valid")
    exit()
    
if FromUnit == "in" and ToUnit == "in":
    multiplier = 1.0
elif FromUnit == "in" and ToUnit == "ft":
    multiplier = (1/12)
elif FromUnit == "in" and ToUnit == "yd":
    multiplier = (1/36)
elif FromUnit == "in" and ToUnit == "mi":
    multiplier = (1/63360)
elif FromUnit == "ft" and ToUnit == "in":
    multiplier = 12
elif FromUnit == "ft" and ToUnit == "ft":
    multiplier = 1.0
elif FromUnit == "ft" and ToUnit == "yd":
    multiplier = 0.333333
elif FromUnit == "ft" and ToUnit == "mi":
    multiplier = 0.000189394
elif FromUnit == "yd" and ToUnit == "in":
    multiplier = 36
elif FromUnit == "yd" and ToUnit == "ft":
    multiplier = 3
elif FromUnit == "yd" and ToUnit == "yd":
    multiplier = 1.0
elif FromUnit == "yd" and ToUnit == "mi":
    multiplier = 0.000568182
elif FromUnit == "mi" and ToUnit == "in":
    multiplier = 63360
elif FromUnit == "mi" and ToUnit == "ft":
    multiplier = 5280
elif FromUnit == "mi" and ToUnit == "yd":
    multiplier = 1760
elif FromUnit == "mi" and ToUnit == "mi":
    multiplier = 1.0

ToValue=FromValue * multiplier
print(FromValue, FromUnit, "=>", ToValue, ToUnit)
