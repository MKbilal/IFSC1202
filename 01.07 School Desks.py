a = int(input('How many Students in class A: '))
b = int(input('How many Students in class B: '))
c = int(input('How many Students in class C: '))

import math

desk = math.ceil(a/2) + math.ceil(b/2) + math.ceil(c/2)

print(desk)
