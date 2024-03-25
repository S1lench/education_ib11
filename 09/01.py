num_items = int(input())
shopping_list = []

for _ in range(num_items):
    item = input()
    shopping_list.append(item)

for item in shopping_list:
    print(item)
