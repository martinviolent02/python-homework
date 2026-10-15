n = int(input())
sum = 1

for i in range(n):
    number = int(input())

    if number != 0:
        sum *= number

print(sum)