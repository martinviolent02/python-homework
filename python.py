
n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num * 3)

print(*numbers)
