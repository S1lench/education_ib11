n = int(input().strip())


phone_book = {}

for _ in range(n):
    entry = input().strip().split()
    phone_number = entry[0]
    name = " ".join(entry[1:])

    if name in phone_book:
        phone_book[name].append(phone_number)
    else:
        phone_book[name] = [phone_number]

m = int(input().strip())

for _ in range(m):
    query_name = input().strip()
    if query_name in phone_book:
        print(" ".join(phone_book[query_name]))
    else:
        print("Нет в телефонной книге")
