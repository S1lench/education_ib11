num_lines = int(input())

data = []
for _ in range(num_lines):
    line = input()
    data.append(line)

search_query = input()

for line in data:
    if search_query in line:
        print(line)
