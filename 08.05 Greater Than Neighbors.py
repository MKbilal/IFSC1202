s = input("Enter Values Separated by Spaces: ")

count=0

for i in range(2,len(s)-2,2):
    if(s[i]>s[i-2]and s[i]>s[i+2]):

        count=count+1
print(count)