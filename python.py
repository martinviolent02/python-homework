
text = input()

if text.startswith('Не') or text.startswith('не'):
    text = text[2:]

print(text.strip())
