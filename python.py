
n = int(input())

for i in range(n):
    text = input()

    if text.startswith('####'):
        continue
    elif text.startswith('%%'):
        print(text[2:])
    else:
        print(text)
