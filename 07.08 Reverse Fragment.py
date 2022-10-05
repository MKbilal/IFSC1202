x = input("Enter a string: ")
Number_1 = -1
Number_2 = -1
for y in range(len(x)):
    if x[y] == 'h':
        if Number_1 == -1:
            Number_1 = y
        Number_2 = y

if Number_1 != Number_2:
    print(x[:Number_1] + x[Number_1:Number_2 + 1][::-1] + x[Number_2 + 1:])
else:
    print(x)