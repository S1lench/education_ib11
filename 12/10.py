input_string = input()

count = 0
for char in input_string:
    if char != ' ' and char != '\t':
        count += 1

print(count)
