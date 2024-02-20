low = 1
high = 1000
attempts = 0
while low <= high and attempts < 10:
    guess = (low + high) // 2
    print(guess)
    response = input()
    if response == '>':
        low = guess + 1
    elif response == '<':
        high = guess - 1
    elif response == '=':
        print('Ура! Я угадал число!')
    else:
        print('Некорректный ввод. Попробуйте снова.')
attempts += 1
print('Я не смог угадать число за 10 попыток. Попробуйте снова.')
