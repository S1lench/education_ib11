sum_numbers = 0
count = 0

while True:
    num = int(input("Введите целое число (для остановки введите 0): "))

    if num == 0:
        break

    sum_numbers += num
    count += 1

    if sum_numbers == 10:
        break

print("Количество введенных чисел в момент, когда их сумма впервые стала равна 10:", count)
