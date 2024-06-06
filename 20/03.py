def calculate_average_height():
    total_height = 0
    count = 0

    print("Введите рост учеников. Оставьте строку пустой и нажмите Enter для завершения.")

    while True:
        height = input("Рост (в см): ").strip()
        if height == '':
            break
        try:
            height = int(height)
            if height > 0:
                total_height += height
                count += 1
            else:
                print("Ошибка: рост должен быть положительным числом.")
        except ValueError:
            print("Ошибка: введите целое число для роста.")

    if count == 0:
        print("-1")
    else:
        average_height = total_height / count
        print(f"Средний рост: {average_height:.2f} см")


if __name__ == "__main__":
    calculate_average_height()
