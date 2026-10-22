
n = int(input())
words = []

for i in range(n):
    word = input()
    words.append(word)

words = sorted(words)

for word in words:
    print(word)
