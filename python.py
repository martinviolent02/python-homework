
n = int(input())
words = []

for i in range(n):
    word = input()
    words.append((len(word), word))

for item in words:
    print(item)
