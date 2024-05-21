text = input().strip()

text = text.lower()

frequency = {}
for char in text:
    if char != ' ':
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

max_frequency = -1
most_frequent_char = ''

for char in frequency:
    if frequency[char] > max_frequency:
        max_frequency = frequency[char]
        most_frequent_char = char
    elif frequency[char] == max_frequency:
        if char < most_frequent_char:
            most_frequent_char = char

print(most_frequent_char)
