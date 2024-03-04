n = int(input())

named_cities = set()

for i in range(n):
    city = input().strip()
    named_cities.add(city)

new_city = input().strip()

if new_city in named_cities:
    print("TRY ANOTHER")
else:
    print("OK")
