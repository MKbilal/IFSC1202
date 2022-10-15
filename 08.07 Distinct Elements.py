a = input("Enter Values Separated by Spaces: ")

list = a.split()

b = len(set(list))

print("Number of Distinct Elements: ", b)