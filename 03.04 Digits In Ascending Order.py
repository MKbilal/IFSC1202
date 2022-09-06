x = int(input('Enter a number: '))

a = x % 10
b = (x // 10) % 10
c = (x // 100) % 10

if c <= b <= a:
    print("YES")
else:
    print("NO")