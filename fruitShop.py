fruits = str(input())
dayOfTheWeek = str(input())
quantity = float(input())
price = 0

if dayOfTheWeek in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruits == "banana":
        price = 2.50
    elif fruits == "apple":
        price = 1.20
    elif fruits == "orange":
        price = 0.85
    elif fruits == "grapefruit":
        price = 1.45
    elif fruits == "kiwi":
        price = 2.70
    elif fruits == "pineapple":
        price = 5.50
    elif fruits == "grapes":
        price = 3.85
elif dayOfTheWeek in ["Saturday", "Sunday"]:
    if fruits == "banana":
        price = 2.70
    elif fruits == "apple":
        price = 1.25
    elif fruits == "orange":
        price = 0.90
    elif fruits == "grapefruit":
        price = 1.60
    elif fruits == "kiwi":
        price = 3.00
    elif fruits == "pineapple":
        price = 5.60
    elif fruits == "grapes":
        price = 4.20
else:
    print("error")
    exit()

if price == 0:
    print("error")
else:
    howMuch = round(price * quantity, 2)
    print("{:.2f}".format(howMuch))
