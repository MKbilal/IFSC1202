x = int(input("Enter a 3 Digit Number: "))
y = 0
for z in range(0,3):
    y += x % 10
    x = x // 10

print("Sum of Digits: {}".format(y))

