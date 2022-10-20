rows, columns = tuple([int(x) for x in input("Enter the number of rows and columns: ").split()])
data = []
for i in range(rows):
    values = input("Enter a line of data: ").split()
    data.append([int(x) for x in values])

for row in data:
    for value in row:
        print(value, end=" ")
    print()

row, col = 0, 0
for i in range(rows):
    for j in range(columns):
        if data[i][j] > data[row][col]:
            rowH, colH = i, j

print("The maximum value", data[row][col], "occurred in row", row, "and column", col)