import sys
no_of_rows,no_of_cols = input("Enter the Number of Rows and Columns: ").split(" ")
no_of_cols=int(no_of_cols)
no_of_rows=int(no_of_rows)

my_matrix = [[0 for i in range(no_of_rows)] for j in range(no_of_cols)]

for i in range(no_of_rows) :
    my_matrix[i]=list(map(int, input("Enter a line of data: ").split(" ")))

if(len(my_matrix[i])>no_of_cols) :
    sys.exit("Invalid entry for Columns")

for i in range(no_of_rows) :
    for j in range(no_of_cols):
        print(my_matrix[i][j], end = " ")

print()

maximum_number=my_matrix[0][0]
minimum_row_index=0
minimum_column_index=0

for i in range(no_of_rows) :
    for j in range(no_of_cols):
        if(my_matrix[i][j] > maximum_number) :
            maximum_number = my_matrix[i][j]
minimum_row_index=i
minimum_column_index=j

print("The maximum value "+str(maximum_number)+" occured in row "+str(minimum_row_index)+" column "+str(minimum_column_index))
