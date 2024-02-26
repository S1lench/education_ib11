number = int(input("Введите натуральное число: "))

count_divisors = 0

for i in range(1, number + 1):
    if number % i == 0:
        count_divisors += 1

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=' ')

if count_divisors == 2:
    print("\nПРОСТОЕ")
else:
    print("\nНЕТ")
