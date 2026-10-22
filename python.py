
previous = input()

while True:
    word = input()

    if word[0] != previous[-1]:
        print(word)
        break

    previous = word
