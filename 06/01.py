print("Введите номера домов с первого листка (для завершения введите пустую строку):")
numbers1 = set()
while True:
    number = input().strip()
    if not number:
        break
    numbers1.add(number)

print("Введите номера домов со второго листка (для завершения введите пустую строку):")
numbers2 = set()
while True:
    number = input().strip()
    if not number:
        break
    numbers2.add(number)

common_numbers = numbers1 & numbers2
if common_numbers:
    print("Номера домов, которые встречаются на обоих листках:")
    for number in common_numbers:
        print(number)
else:
    print("EMPTY")
