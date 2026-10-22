
m = int(input())
dishes = []

for i in range(m):
    dish = input()
    dishes.append(dish)

n = int(input())
cooked = []

for i in range(n):
    day = input().split()

    for dish in day:
        cooked.append(dish)

for dish in dishes:
    if dish not in cooked:
        print(dish)
