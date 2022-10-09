str = input('Enter a string: ')
x = -1
y = -1

for index in range(len(str)):
    if x == -1 and str[index] == 'f':
        x = index
        y = index
    elif str[index] == 'f':
        y = index

if x == -1:
    print('0')
elif x == y:
    print(x)
else:
    print(x,y)