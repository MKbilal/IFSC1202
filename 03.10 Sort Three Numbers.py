#Prompt for three integers and print them in ascending order.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

a = min(x, y, z)
b = max(x, y, z)
c = (x + y + z) - a - b
print(a, c, b)
