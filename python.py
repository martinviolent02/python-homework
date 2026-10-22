
white_list = []

while True:
    word = input()
    if word == "":
        break
    white_list.append(word)

while True:
    query = input()
    if query == "":
        break
    if query in white_list:
        print(query)
