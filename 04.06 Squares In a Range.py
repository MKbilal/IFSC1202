# Python program to count squares between a and b
 
def CountSquares(a, b):
 
    cnt = 0 # initialize result
 
    # Traverse through all numbers
    for i in range (a, b + 1):
        j = 1;
        while j * j <= i:
            if j * j == i:
                 cnt = cnt + 1
            j = j + 1
        i = i + 1
    return cnt
 
# Driver Code
a = 9
b = 25
print ("Count of squares is:", CountSquares(a, b))