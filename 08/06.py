max_length = int(input())
num_titles = int(input())

for _ in range(num_titles):
    title = input().strip()
    if len(title) <= max_length:
        print(title)
    else:
        print(title[:max_length-3] + '...')
