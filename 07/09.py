message = input("Введите сообщение: ")
letter_number = int(input("Введите номер буквы: "))
if letter_number < 1 or letter_number > len(message):
    print("ОШИБКА")
else:
    print(message[letter_number - 1])