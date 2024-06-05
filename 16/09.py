base = ['Лина', 'Ангелина Мухаметдинова']


def hello(name):
    print(f'Здравствуйте, {name}! Вашу карту ищут...')


def search_card(name):
    global base
    if name in base:
        card_number = base.index(name) + 1
        print(f'Ваща карта найдена с номером {card_number} найдена')
    else:
        print('Ваша карта не найдена')


hello('Лина')
search_card('Лина')
hello('Ангелина Мухаметова')
search_card('Ангелина Мухаметова')