n = int(input())
n = abs(n)

count = 0

while n > 0:
    n //= 10
    count += 1

print(count)