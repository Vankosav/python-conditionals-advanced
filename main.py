num = int(input())
if num == 1:
    print('Monday')
elif num == 2:
    print('Tuesday')
elif num == 3:
    print('Wednesday')
elif num == 4:
    print('Thursday')
elif num == 5:
    print('Friday')
elif num == 6:
    print('Saturday')
elif num == 7:
    print('Sunday')
else:
    print('Error')

dayOfTheWeek = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

print(dayOfTheWeek.get(num, "Error"))



