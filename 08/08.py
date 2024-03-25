coin_tosses = input()

max_heads_in_row = 0
current_heads_in_row = 0

for result in coin_tosses:
    if result == 'о':
        current_heads_in_row += 1
    else:
        current_heads_in_row = 0
    max_heads_in_row = max(max_heads_in_row, current_heads_in_row)

print(max_heads_in_row)
