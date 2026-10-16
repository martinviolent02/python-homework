total = 0
count = 0
result = -1

while True:
    n = int(input())

    if n == 0:
        break

    total += n
    count += 1

    if total == 10:
        result = count
        break

print(result)