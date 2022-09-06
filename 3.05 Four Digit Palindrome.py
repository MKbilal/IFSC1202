x = int(input('Enter a number: '))

a = x % 10
b = (x // 10) % 10
c = (x // 100) % 10
d = (x // 1000) % 10

if a == d and b == c:
    print("YES")
else:
    print("NO")


