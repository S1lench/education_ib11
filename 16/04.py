items = []
total_items = 0
receipt_count = 0


def add_items(item_name, item_cost):
    global items, total_items
    items.append((item_name, item_cost))
    total_items += 1


def print_receipt():
    global items, total_items, receipt_count
    if total_items == 0:
        return
    receipt_count += 1
    print(f'Чек {receipt_count}. Всего предметов: {total_items}')
    for item_name, item_cost in items:
        print(f'{item_name} - {item_cost}')
    total_cost = sum(item[1] for item in items)
    print('Итого:', total_cost)
    print('-----')
    items = []
    total_items = 0


add_items('Блокнот', 100)
print_receipt()

add_items('Ручка', 70)
print_receipt()
print_receipt()

add_items('Булочка', 15)
add_items('Булочка', 15)
add_items('Чай', 5)
print_receipt()

add_items('Булочка', 15)
add_items('Булочка', 15)
# (отменить чек) - этот чек не печатаем
