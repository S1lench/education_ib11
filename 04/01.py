weeks = 0
while True:
    temp = float(input("Введите максимальную дневную температуру: "))
    if temp >= 22.0:
        break
    weeks += 1

weeks //= 7
print("Количество полных недель:", weeks)
