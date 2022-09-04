a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if a < b & a < c :
    x = a
elif b < c:
    x = b
else:
    x = c
print(x)
