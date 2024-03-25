secret = input()
guess = input()

bulls = sum(1 for s, g in zip(secret, guess) if s == g)
cows = sum(1 for s in secret if s in guess) - bulls

print(bulls, cows)
