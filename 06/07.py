M = int(input())

all_lessons_students = set()

first_lesson_students = set(input().split())

all_lessons_students.update(first_lesson_students)

for _ in range(M - 1):
    lesson_students = set(input().split())
    all_lessons_students.intersection_update(lesson_students)

for student in all_lessons_students:
    print(student)
