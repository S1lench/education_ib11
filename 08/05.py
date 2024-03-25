N = int(input())

for _ in range(N):
    advice = input().strip()
    if advice[:3].lower() == "не ":
        print(advice[3:])
    else:
        print(advice)
