input_str = input().strip()
robotic_str = '-'.join('-'.join(word.upper()) for word in input_str.split())
print(robotic_str)
