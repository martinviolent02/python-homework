count = 0
cat_count = 0
first_cat = -1

while True:
    text = input()

    if text == "СТОП":
        break

    count += 1

    if "кот" in text or "Кот" in text:
        cat_count += 1

        if first_cat == -1:
            first_cat = count

print(cat_count)
print(first_cat)