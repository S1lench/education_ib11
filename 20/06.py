def extract_comments_with_line_numbers(program_text):
    lines = program_text.split('\n')

    comments_with_numbers = []

    for line_number, line in enumerate(lines, 1):
        if line.strip().startswith('#'):
            comments_with_numbers.append(f"{line_number}: {line.strip().lstrip('#').strip()}")
    return comments_with_numbers

with open('python.txt', 'r') as file:
    program_text = file.read()

comments = extract_comments_with_line_numbers(program_text)

for comment in comments:
    print(comment)
