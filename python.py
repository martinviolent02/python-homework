
n = int(input())
students = []

for i in range(n):
    surname, grade = input().split()
    students.append((surname, int(grade)))

for surname, grade in students:
    print(surname, grade)

print()

for surname, grade in students:
    if grade == 4 or grade == 5:
        print(surname, grade)
