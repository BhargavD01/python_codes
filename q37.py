#37 Prompt the user for two 2D matrices (lists of lists) of the same dimensions. Perform matrix addition and print the result.
# didnt understand
# Get dimensions of the matrices
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Get the first matrix
print("Enter the first matrix:")
matrix1 = [list(map(int, input().split())) for _ in range(rows)]

# Get the second matrix
print("Enter the second matrix:")
matrix2 = [list(map(int, input().split())) for _ in range(rows)]

# Perform matrix addition
result_matrix = []
for i in range(rows):
    result_row = []
    for j in range(cols):
        result_row.append(matrix1[i][j] + matrix2[i][j])
    result_matrix.append(result_row)

# Print the result
print("Result of matrix addition:")
for row in result_matrix:
    print(row)