words = []
while True:
    word = input()
    if word == "стоп":
        break
    words.append(word)

shortest = min(words, key=len)
longest = max(words, key=len)

letters_in_longest = set(longest)
letters_in_shortest = set(shortest)

if letters_in_shortest.issubset(letters_in_longest):
    print("ДА")
else:
    print("НЕТ")
