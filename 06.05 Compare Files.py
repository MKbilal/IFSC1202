x = open("06.05 CompareFileA.txt")
y = open("06.05 CompareFileB.txt")
Number_x = [] 
Number_y = []
for l in x:
    Number_x.append(l)
for l in y:
    Number_y.append(l)
z = 0
for x in range(len(Number_x)):
    if(Number_x[x] != Number_y[x]):
        print(f"Line :{x+1} - {Number_x[x]}")
        print(f"Line :{x+1} - {Number_y[x]}")
        z += 1
print(z,"differences")
