n = int(input("Введите количество секунд до запуска: "))

if n < 0:
    print("Пуск")
else:
    for i in range(n, -1, -1):
        print("Осталось секунд:", i)
    print("Пуск")
