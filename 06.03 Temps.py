file = open("06.03 FTemps.txt")
Numbers = 0
for F in file:
    C = (float(F) - 32)*5/9
    f = open("06.03 CTemps.txt")
    Numbers = Numbers + 1
print(str(Numbers)+" records written")