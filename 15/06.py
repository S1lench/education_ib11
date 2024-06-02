def print_document(pages):
    secret = False
    for page in pages:
        if page.startswith("Секретно"):
            secret = True
            break
        print(page)

    if secret:
        print("Дальнейшие материалы засекречены")
    else:
        print("Напечатано без купюр")


print_document(["Обычная страница", "И еще страница", "Секретно Вот этот вот текст не показывать", "Никому", "Никогда"])
print_document(["Пустой трёп", "который", "никому не интересен"])
