from_value = float(input("Enter From Value: "))
from_unit = input("Enter From Unit (mm,cm,m,km,in,yd,mi): ")
to_unit = input("Enter To Unit(mm,cm,m,km,in,yd,mi): ")
arr = []

with open("09.04 Conversion.txt","r") as file:
    arr.append(file.readline().strip().split())
    for line in file.readlines():
        data = line.strip().split()
        for i in range(1,len(data)):
            data[i] = float(data[i])
        arr.append(data)

from_index,to_index = -1, -1

for i in range(len(arr)):
    if arr[i][0] == from_unit:
        from_index = i

if from_index == -1:
    print("FromUnit is not valid")
    exit(0)

for i in range(len(arr[0])):
    if arr[0][i] == to_unit:
        to_index = i

if to_index == -1:
    print("ToUnit is not valid")
    exit(0)

res = round(from_value * arr[from_index][to_index],7)
print("{:.1f} {} => {} {}".format(from_value,from_unit,res,to_unit))
