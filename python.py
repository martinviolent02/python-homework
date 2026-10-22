
shift = int(input())
text = input()

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
result = ''

for letter in text:
    if letter in alphabet:
        index = alphabet.index(letter)
        new_index = (index + shift) % len(alphabet)
        result += alphabet[new_index]
    else:
        result += letter

print(result)
