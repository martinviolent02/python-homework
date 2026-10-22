n = int(input())
names = []

for i in range(n):
    name = input()
    names.append(name)

count = 0

for name in names:
    if names.count(name) > 1:
        count += 1

print(count)