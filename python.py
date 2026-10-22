
n = int(input())
letters = {}

for i in range(n):
    position, letter = input().split()
    letters[int(position)] = letter

for i in range(1, n + 1):
    print(letters[i], end="")
