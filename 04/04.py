n = int(input("Введите целое неотрицательное число: "))
factorial = 1

if n < 0:
    print("Факториал определен только для неотрицательных чисел.")
else:
    for i in range(1, n + 1):
        factorial *= i

    print("Факториал числа", n, "равен", factorial)
