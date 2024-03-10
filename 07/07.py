message = input()
codes = []

for char in message:
    char_code = str(ord(char))
    codes.append(char_code)

codes_joined = ",".join(codes)

print(codes_joined)
