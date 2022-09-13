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