found = False

while True:
    text = input()

    if text == "СТОП":
        break

    if "пёс" in text or "Пёс" in text:
        found = False
    elif "кот" in text or "Кот" in text:
        found = True

if found:
    print("МЯУ")
else:
    print("НЕТ")