M = int(input())

available_dishes = set()

for _ in range(M):
    dish = input().strip()
    available_dishes.add(dish)

N = int(input())

cooked_dishes = set()

for _ in range(N):
    dishes_count = int(input())
    for _ in range(dishes_count):
        dish = input().strip()
        cooked_dishes.add(dish)

not_cooked_dishes = available_dishes - cooked_dishes

for dish in not_cooked_dishes:
    print(dish)
