
n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

for i in range(n - 1):
    print(numbers[i] + numbers[i + 1], end=' ')
