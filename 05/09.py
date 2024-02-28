num_lines = int(input("Введите количество строк: "))

cat_found = False
dog_found = False

for _ in range(num_lines):
    line = input("Введите строку: ")

    if "Кот" in line or "кот" in line:
        cat_found = True
    if "Пёс" in line or "пёс" in line:
        dog_found = True

    if dog_found:
        cat_found = False
    elif cat_found:
        continue

if cat_found:
    print("МЯУ")
else:
    print("НЕТ")
