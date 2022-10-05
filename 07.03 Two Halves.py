x = input("Enter a string: ")

y = int(len(x)/2)

print(x[y:] + x[:y])