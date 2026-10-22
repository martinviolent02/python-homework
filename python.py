
n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

unique_numbers = set(numbers)

print(len(unique_numbers))
