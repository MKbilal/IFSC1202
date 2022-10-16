numbers = input("Enter Values Separated by Spaces: ").split()
for x in range(len(numbers)):
    numbers[x] = int(numbers[x])

print("Unique Elements: ", end = '')
for x in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[x] == numbers[j]:
            count += 1
    if count == 1:
        print(numbers[x], end = ' ')
print()