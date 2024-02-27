line_number = 0
found_cat_line = -1
while True:
    line = input()
    line_number += 1
    if line == 'стоп':
        break
    if 'кот' in line:
        found_cat_line = line_number
print(found_cat_line)
