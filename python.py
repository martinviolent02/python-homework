
text = input()

count = 1
max_count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        count = 1

    if count > max_count:
        max_count = count

print(max_count)
