letter = input().strip()
sentence = input().strip()

words = sentence.split()

words_with_letter = [word for word in words if letter.lower() in word.lower()]

for word in words_with_letter:
    print(word)
