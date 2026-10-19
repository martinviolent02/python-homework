m = int(input())
common = None

for i in range(m):
    k = int(input())
    students = set()

    for j in range(k):
        name = input()
        students.add(name)

    if common is None:
        common = students
    else:
        common = common & students

for name in common:
    print(name)