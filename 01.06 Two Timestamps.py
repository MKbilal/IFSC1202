print('First Timestamp')
x = int(input('Enter Hour number: '))
y = int(input('Enter Minutes: '))
z = int(input('Enter seconds: '))

print('Second Timestamp')
a = int(input('Enter Hour number: '))
b = int(input('Enter Minutes: '))
c = int(input('Enter seconds: '))

second_1 = (x * 3600 + y * 60 + z)
second_2 = (a * 3600 + b * 60 + c)

total_second = second_1 - second_2

print(abs(total_second))
