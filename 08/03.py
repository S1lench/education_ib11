username = input()

for char in username:
    if not char.isalnum() and char != '_':
        print("Неверный символ:", char)
        break
else:
    print("OK")
