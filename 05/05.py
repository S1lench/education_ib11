line_number = 0
cat_found = False

while True:
    line = input()
    if line == "СТОП":
        break
    line_number += 1
    if "Кот" in line or "кот" in line:
        cat_found = True
        break

if cat_found:
    print(line_number)
else:
    print(-1)
