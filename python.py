
n = int(input())
text = input()

if len(text) > n:
    text = text[:n - 3] + '...'

print(text)
