def transpose(matrix):
    transposed = []
    for j in range(len(matrix[0])):
        transposed_row = []
        for i in range(len(matrix)):
            transposed_row.append(matrix[i][j])
        transposed.append(transposed_row)
    return transposed


matrix = [[1, 2], [3, 4]]
transposed_matrix = transpose(matrix)
for line in transposed_matrix:
    print(*line)
