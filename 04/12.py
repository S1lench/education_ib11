n = int(input("Введите количество чисел: "))

total_sum = 0

for i in range(1, n + 1):
    number = int(input(f"Введите число {i}: "))
    if i % 2 == 1:
        total_sum += number
    else:
        total_sum -= number

print("Знакочередующаяся сумма ряда:", total_sum)
