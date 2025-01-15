#38 Write a function to find the transpose of a given matrix (list of lists).
def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):  # Iterate over columns
        row = []
        for j in range(len(matrix)):  # Iterate over rows
            row.append(matrix[j][i])
        transposed.append(row)
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = transpose(matrix)

# Print the transposed matrix
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)