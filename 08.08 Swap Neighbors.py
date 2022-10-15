lst = input("Enter Values Separated by Spaces: ").split()

for x in range(0, len(lst), 2):
    if x + 1 < len(lst):
        lst[x], lst[x + 1] = lst[x + 1], lst[x]

print("Swapped Values: ", end = '')
for item in lst:
    print(item, end = ' ')
print()