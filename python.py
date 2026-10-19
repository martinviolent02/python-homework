first = set()
second = set()

while True:
    num = input()

    if num == "":
        break

    first.add(num)

while True:
    num = input()

    if num == "":
        break

    second.add(num)

result = first & second

if result:
    print(*result)
else:
    print("EMPTY")