Number = input("Enter Values Separated by Spaces: ")

Numbers = Number.split(" ")

for x in range(len(Numbers)):

    if int(Numbers[x])%2==1:

        print(Numbers[x])