def find_mountain(heightsMap):
    max_height = float('-inf')
    max_row, max_col = 0, 0

    for row in range(len(heightsMap)):
        for col in range(len(heightsMap[0])):
            if heightsMap[row][col] > max_height:
                max_height = heightsMap[row][col]
                max_row, max_col = row, col

    return max_row, max_col


a = [[1, 3, 1], [3, 2, 5], [2, 2, 2]]
row, col = find_mountain(a)
print(row, col)

a = [[2, 4, 2, 3, 2], [3, 2, 3, 4, 3]]
row, col = find_mountain(a)
print(a[row][col])
