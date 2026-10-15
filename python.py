while True:
    password = input()
    repeat = input()

    if len(password) < 8:
        print("Слишком короткий!")
    elif password != repeat:
        print("Пароли не совпадают!")
    elif "123" in password:
        print("Пароль не должен содержать 123!")
    else:
        print("OK")
        break