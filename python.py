count = 0
first_cat = -1

while True:
    text = input()

    if text == "СТОП":
        break

    count += 1

    if first_cat == -1 and ("кот" in text or "Кот" in text):
        first_cat = count

print(first_cat)