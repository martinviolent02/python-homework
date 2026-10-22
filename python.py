
n = int(input())
words = []

for i in range(n):
    word = input()
    words.append(word)

words.sort(key=lambda word: (len(word), word))

for word in words:
    print(word)
