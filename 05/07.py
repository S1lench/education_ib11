N = int(input())  # Количество команд от правительства
war_with = "Евразия"  # Изначально война с Евразией
peace_with = "Остазия"  # Изначально мир с Остазией

for _ in range(N):
    command = input()
    if command == "С кем война?":
        print(war_with)
    elif command == "С кем мир?":
        print(peace_with)
    elif command == "Меняем":
        war_with, peace_with = peace_with, war_with  # Меняем состояние войны и мира

