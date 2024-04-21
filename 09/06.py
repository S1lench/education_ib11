
num_data_lines = int(input("Введите количество строк с данными: "))
data_lines = [input() for _ in range(num_data_lines)]

num_search_lines = int(input("Введите количество поисковых строк: "))
search_lines = [input() for _ in range(num_search_lines)]

for data_line in data_lines:
    found_all = True
    for search_line in search_lines:
        if search_line not in data_line:
            found_all = False
            break
    if found_all:
        print(data_line)
