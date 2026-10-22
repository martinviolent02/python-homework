
n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

last = numbers[-1]
found = False

for i in range(n - 1):
    for j in range(i + 1, n - 1):
        if numbers[i] * numbers[j] == last:
            found = True

if found:
    print("ДА")
else:
    print("НЕТ")
