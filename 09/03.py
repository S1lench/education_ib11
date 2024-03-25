num_lines = int(input())

lines = []
for _ in range(num_lines):
    line = input()
    lines.append(line)

letter_index = int(input())

for line in lines:
    if len(line) >= letter_index:
        print(line[letter_index - 1], end='')
print()
