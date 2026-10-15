n = int(input())
sum = 0

for i in range(n):
    number = int(input())

    if i % 2 == 0:
        sum += number
    else:
        sum -= number

print(sum)