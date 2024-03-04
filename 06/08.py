N = int(input())

surnames = set()

for _ in range(N):
    surname = input().strip()
    surnames.add(surname)

print(N - len(surnames))
