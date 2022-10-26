n_file = open("Exam Two Names.txt")

gn = []
bn = []

for line in n_file.readlines():
    data = line.strip().split(',')
    bn.append(data[0].strip())
    gn.append(data[1].strip())
n_file.close()
n = input('Enter a name: ').strip()
while n.lower() != 'q':
    n = n[0].upper() + n[1:].lower()
    if n in gn:
        print("Girl's Name - Rank", gn.index(n) + 1)
    elif n in bn:
        print("Boys's Name - Rank", bn.index(n) + 1)
    else:
        print('Name not found')

    n = input('Enter a name: ').strip()