n = int(input('Введите количество строк: '))
found_cat = False

for i in range(n):
    line = input('Введите строку: ')
    if 'кот' in line or 'Кот' in line:
        found_cat = True
        break
if found_cat:
    print('МЯУ')
else:
    print('НЕЕЕЕЕЕТ')
