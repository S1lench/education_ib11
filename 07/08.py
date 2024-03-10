n = int(input())

while 1 < n > 1 and n < 1000000000:
    first_digit = int(str(n)[0])
    n *= first_digit
    if first_digit == 1:
        break

print(n)
