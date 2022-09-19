#A palindrome is a number which reads the same when read forward as it it does when read backward.
#Given a four-digit integer, print "YES" if it's a palindrome and print "NO" otherwise.
#Hint: put the units, tens, hundreds, and thousands in separate variables. Do not use any string functions.

x = int(input('Enter a number: '))

a = x % 10
b = (x // 10) % 10
c = (x // 100) % 10
d = (x // 1000) % 10

if a == d and b == c:
    print("YES")
else:
    print("NO")


