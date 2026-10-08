print('Ты любишь программирование?')
a = input()
print('Ты любишь python?')
b = input()
if a == 'да' and b == 'да':
    print('Молодец')
if a == 'да' and b == 'нет':
    print('Ну хорошист')
if a == 'нет' and b == 'да':
    print('Ну пойдет')
if a == 'нет' and b == 'нет':
    print('Ужас')