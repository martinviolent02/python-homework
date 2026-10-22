
n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

p = int(input())
q = int(input())

print(sum(numbers[p:q + 1]))
