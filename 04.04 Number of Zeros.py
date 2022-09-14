N = int(input('Enter N: '))
count = 0
for i in range(N):
    value = int(input('Enter Number: '))
    if value == 0:
        count += 1
print('Number of Zeros:', count)