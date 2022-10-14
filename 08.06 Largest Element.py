integers = input("Enter Values Separated by Spaces: ")
integers = [int(i) for i in integers.split()]
index = 0
largest_val = integers[0]
for i in range(len(integers)):
    if integers[i] > largest_val:
        largest_val = integers[i]
        index = i
print(f'Largest Value: {largest_val}')
print(f'Index of Largest Value: {index}')