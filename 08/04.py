size = int(input())

for row in range(size, 0, -1):
    for col in range(65, 65 + size):
        print(chr(col) + str(row), end=" ")
    print()
