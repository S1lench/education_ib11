count = 0
first_cat_line = -1
line_number = 0

while True:
    line = input()
    line_number += 1

    if line == "СТОП":
        break

    if "кот" in line:
        count += 1
        if first_cat_line == -1:
            first_cat_line = line_number

print(count, first_cat_line)
