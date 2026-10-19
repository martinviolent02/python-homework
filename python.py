m = int(input())
english = set()

for i in range(m):
    name = input()
    english.add(name)

n = int(input())
german = set()

for i in range(n):
    name = input()
    german.add(name)

result = english ^ german

if result:
    print(len(result))
else:
    print("NO")