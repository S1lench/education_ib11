N = int(input())

for i in range(N):
    line = input()
    if 'кот' in line:
        start_index = line.find('кот') + 1
        print(i + 1, start_index)
