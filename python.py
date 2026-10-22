
n = int(input())
people = []

for i in range(n):
    surname, height = input().split()
    people.append((surname, int(height)))

people.sort(key=lambda person: person[1], reverse=True)

for surname, height in people:
    print(surname, height)
