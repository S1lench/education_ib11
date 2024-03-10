first_word = input()
while True:
    second_word = input()
    if first_word[-1] != second_word[0]:
        print(second_word)
        break
    first_word = second_word
