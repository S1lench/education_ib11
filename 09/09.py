num_clients = int(input("Введите количество клиентов: "))
savings = [int(input()) for _ in range(num_clients)]

print("Текущие накопления каждого клиента:")
for saving in savings:
    print(saving)

print()

print("Накопления каждого клиента после увеличения доходности на 200%:")
for saving in savings:
    print(saving * 3)
