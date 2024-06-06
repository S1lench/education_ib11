def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiouy')


def count_consonants(s):
    return sum(1 for char in s if char.lower() not in 'aeiouy')


def ask_password(login, password, success, failure):
    login = login.lower()
    password = password.lower()
    vowels_login = count_vowels(login)
    consonants_login = count_consonants(login)
    vowels_password = count_vowels(password)
    consonants_password = count_consonants(password)

    if vowels_password != 3 or consonants_password != consonants_login:
        if vowels_password != 3 and consonants_password != consonants_login:
            failure(login, "Everything is wrong")
        elif vowels_password != 3:
            failure(login, "Wrong number of vowels")
        else:
            failure(login, "Wrong consonants")
    else:
        success(login)


def main(login, password):
    def success(login):
        print(f'Привет, {login}')

    def failure(login, error):
        print(f'Кто-то пытался притвориться пользователем {login}, но в пароле допустил ошибку: {error}')

    ask_password(login, password, success, failure)


main("login", "luagon")
main("login", "aaalgn")
main("login", "aaalggn")
main("login", "lmg")
main("login", "qwerty")