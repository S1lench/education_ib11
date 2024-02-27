a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
for num in range(a, b+1):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
