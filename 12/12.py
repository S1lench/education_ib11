input_string = input().strip()

input_string = input_string.lower()

char_count = {}

for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

max_occurrences = max(char_count.values())
print(max_occurrences)
