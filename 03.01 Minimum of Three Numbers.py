a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
d = int(input('Enter fourth number: '))

if a < b & a < c & a < d:  #a is smaller than b and c
    x = a
elif b < c & b < a & b < d:     # b is smaller than c 
    x = b
elif c < d & c < a & c < d: # c is smaller d
    x = c
else:
    x = d
print(x)


