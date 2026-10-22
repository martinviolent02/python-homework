
text = input()
codes = []

for letter in text:
    codes.append(str(ord(letter)))

print(', '.join(codes))
