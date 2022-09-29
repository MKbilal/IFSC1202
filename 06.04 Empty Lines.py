x = '06.04 EmptyLinesInput.txt'
y = '06.04 EmptyLinesOutput.txt'
Number_1 = 0
Number_2 = 0
with open(x) as f:
    for line in f:
        Number_1 += 1
        if line.strip():
            Number_2 += 1
print(Number_1,'records read')
print(Number_2,'records written')

