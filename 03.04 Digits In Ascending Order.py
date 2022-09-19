#Given a three-digit integer, print "YES" if its digits are in ascending order left to right, print "NO" otherwise.
#Do not try to sort the number. Determine each digit and use "if" statements.


x = int(input('Enter a number: '))

a = x % 10
b = (x // 10) % 10
c = (x // 100) % 10

if c <= b <= a:
    print("YES")
else:
    print("NO")
