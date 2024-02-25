city = str(input())
salesVolume = float(input())

if 0 <= salesVolume <= 500:
    if city == "London":
        print("{:.2f}".format(round(salesVolume * 0.05, 2)))
    elif city == "Paris":
        print("{:.2f}".format(round(salesVolume * 0.045, 2)))
    elif city == "Rome":
        print("{:.2f}".format(round(salesVolume * 0.055, 2)))
elif 500 <= salesVolume <= 1000:
    if city == "London":
        print("{:.2f}".format(round(salesVolume * 0.07, 2)))
    elif city == "Paris":
        print("{:.2f}".format(round(salesVolume * 0.075, 2)))
    elif city == "Rome":
        print("{:.2f}".format(round(salesVolume * 0.08, 2)))
elif 1000 <= salesVolume <= 10000:
    if city == "London":
        print("{:.2f}".format(round(salesVolume * 0.08, 2)))
    elif city == "Paris":
        print("{:.2f}".format(round(salesVolume * 0.10, 2)))
    elif city == "Rome":
        print("{:.2f}".format(round(salesVolume * 0.12, 2)))
elif salesVolume > 10000:
    if city == "London":
        print("{:.2f}".format(round(salesVolume * 0.12, 2)))
    elif city == "Paris":
        print("{:.2f}".format(round(salesVolume * 0.13, 2)))
    elif city == "Rome":
        print("{:.2f}".format(round(salesVolume * 0.145, 2)))
elif salesVolume < 0 or city not in ["London", "Paris", "Rome"]:
    print('error')
