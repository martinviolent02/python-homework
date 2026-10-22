
n = int(input())
lines = []

for i in range(n):
    line = input()
    lines.append(line)

word1 = input()
word2 = input()

for line in lines:
    if word1 in line and word2 in line:
        print(line)
