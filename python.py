
n = int(input())
lines = []

for i in range(n):
    text = input()
    lines.append(text)

query = input()

for text in lines:
    if query in text:
        print(text)
