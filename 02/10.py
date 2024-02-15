num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
operation = input('Введите оператор: ')
if num2 == '0' and operation == '/':
    print('888888')
elif operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    print(num1 / num2)
else:
    print('888888')
