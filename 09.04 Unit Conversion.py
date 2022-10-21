fromvalue = float(input("Enter From Value: "))
fromunit = input("Enter From Unit (mm,cm,m,km,in,yd,mi): ")
tounit = input("Enter To Unit(mm,cm,m,km,in,yd,mi): ")
arr = []

with open("09.04 Conversion.txt","r") as file:
    arr.append(file.readline().strip().split())
    for line in file.readlines():
        data = line.strip().split()
        for i in range(1,len(data)):
            data[i] = float(data[i])
        arr.append(data)

fromindex,toindex = -1, -1

for i in range(len(arr)):
    if arr[i][0] == fromunit:
        fromindex = i

if fromindex == -1:
    print("FromUnit is not valid")
    exit(0)

for i in range(len(arr[0])):
    if arr[0][i] == tounit:
        toindex = i

if toindex == -1:
    print("ToUnit is not valid")
    exit(0)

r = round(fromvalue * arr[fromindex][toindex],7)
print("{:.1f} {} => {} {}".format(fromvalue,fromunit,r,tounit))
