
word = input()
n = int(input())

if n >= 1 and n <= len(word):
    print(word[n - 1])
else:
    print('ОШИБКА')
