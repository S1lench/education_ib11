login = input('Введите желаемый логин: ')
email = input('Введите ваш email адрес: ')
if '@' in login:
    print('Некорректный логин')
elif '@' not in email:
    print('Некорректный адрес')
else:
    print('OK')
