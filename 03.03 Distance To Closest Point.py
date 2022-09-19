#Given the coordinates of the three points A, B, and C on a line, print a distance from the point A to closest point to it.
#Hint: Determine the distance from A to B by subtracting B from A, then determine the distance from A to C by subtracting C from A. Determine the smallest distance.

A = int(input("Enter point A: "))
B = int(input("Enter point B: "))
C = int(input("Enter point C: "))

D = abs(B - A)
E = abs(C - A)

if (D > E):
    print(E)


else:
    print(D)




