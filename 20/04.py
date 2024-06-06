with open('python.txt', 'r') as file:
    count_comments = sum(1 for line in file if line.strip().startswith('#'))
print(count_comments)
