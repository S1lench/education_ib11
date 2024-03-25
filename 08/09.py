N = int(input())

for _ in range(N):
    line = input().strip()
    if not line.startswith("####") and not line.startswith("%%"):
        print(line)
