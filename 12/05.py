first_line = input().strip()
N = int(first_line.split()[1])

processed_lines = []
for _ in range(N):
    line = input()
    comment_index = line.find('#')
    if comment_index != -1:
        line = line[:comment_index]
    line = line.rstrip()
    processed_lines.append(line)

for line in processed_lines:
    print(line)
