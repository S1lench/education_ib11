def ask_password():
    correct_password = "password"
    attempts = 3

    while attempts > 0:
        password_attempt = input()
        if password_attempt == correct_password:
            print("Пароль принят")
            break
        else:
            attempts -= 1

    if attempts == 0:
        print("В доступе отказано")
