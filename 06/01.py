list1 = set()
while True:
    num = input()
    if num:
        list1.add(num)
    else:
        break

input()

list2 = set()
while True:
    num = input()
    if num:
        list2.add(num)
    else:
        break

common_numbers = list1.intersection(list2)
if common_numbers:
    for num in common_numbers:
        print(num)
else:
    print('EMPTY')
