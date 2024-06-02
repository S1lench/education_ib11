def space_game(text):
    space_count = text.count(' ')
    if space_count % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")
