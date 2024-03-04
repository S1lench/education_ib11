M = int(input())
N = int(input())

english_students = set()
german_students = set()

for _ in range(M):
    english_students.add(input().strip())

for _ in range(N):
    german_students.add(input().strip())

only_english = len(english_students - german_students)
only_german = len(german_students - english_students)

if only_english == 0 and only_german == 0:
    print("NO")
else:
    print(only_english + only_german)
