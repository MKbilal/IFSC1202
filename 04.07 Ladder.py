n = int(input("Enter the number: "))
if n <= 9:
    for x in range(1, n + 1):
        for y in range(1, x + 1):
            print(y, sep = "", end = "")
        print()
else:
    print("Number is too big")