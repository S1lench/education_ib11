def has_top_students():
    try:
        n_classes = int(input("Введите количество классов: ").strip())
    except ValueError:
        print("Ошибка: Введите целое число для количества классов.")
        return

    for class_index in range(n_classes):
        try:
            n_students = int(input(f"\nВведите количество учеников в классе {class_index + 1}: ").strip())
        except ValueError:
            print(f"Ошибка: Введите целое число для количества учеников в классе {class_index + 1}.")
            return

        has_top_student = False
        for student_index in range(n_students):
            try:
                surname, grade = input(
                    f"Введите фамилию и оценку ученика {student_index + 1} через пробел: ").strip().split()
                grade = int(grade)
                if grade == 5:
                    has_top_student = True
            except ValueError:
                print(
                    f"Ошибка: Некорректный ввод. Пожалуйста, введите данные в формате 'Фамилия Оценка' для ученика {student_index + 1}.")
                return

        if not has_top_student:
            print("НЕТ")
            return

    print("ДА")


if __name__ == "__main__":
    has_top_students()
