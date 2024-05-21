N = int(input())
lines = [input() for _ in range(N)]

for i, line in enumerate(lines):
    index = line.find('кот')
    if index != -1:
        print(i + 1, index + 1)
