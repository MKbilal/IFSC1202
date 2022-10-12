Numbers = input("Enter Values Separated by Spaces: ")

numbers = Numbers.split()

arr=[]

for num in numbers:
    arr.append(num)

for x in range(0,len(arr)):
    if(x % 2 !=0):
        print(arr[x],end="\n")
