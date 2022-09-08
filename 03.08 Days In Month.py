month = int(input("Enter month: "))

if month in [9, 4, 6, 11]:
    print (30)

elif month in [1, 3, 5, 7, 8, 10, 12]:
    print (31) 
else:
    print(28)