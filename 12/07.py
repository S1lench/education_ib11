expression = input().strip().split()

stack = []

for token in expression:
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()

        if token == '+':
            stack.append(a + b)
        elif token == '-':
            stack.append(a - b)
        elif token == '*':
            stack.append(a * b)
        else:
            raise ValueError(f"Неизвестный оператор: {token}")

result = stack.pop()
print(result)
