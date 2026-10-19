n = int(input())
words = set()

for i in range(n):
    word = input()
    words.add(word)

print(len(words))