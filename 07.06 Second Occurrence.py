x = input("Enter a string: ")

index = x.find('f')
if index == -1:
    print("Zero f")
else:
    index = x.find('f', index + 1)
    if index == -1:
        print("One f")
    else:
        print(index)