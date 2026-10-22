
name = input()

allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

for symbol in name:
    if symbol not in allowed:
        print('Неверный символ:', symbol)
        break
else:
    print('OK')
