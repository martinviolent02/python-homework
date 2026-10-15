while True:
    temp = float(input())

    if temp == 0:
        break
    elif temp < 15.5:
        print("ХОЛОДНО")
    elif temp > 28:
        print("ЖАРКО")
    else:
        print("НОРМАЛЬНО")