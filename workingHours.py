hourOfTheDay = int(input())
dayOfTheWeek = str(input())

valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if 10 <= hourOfTheDay <= 18 and dayOfTheWeek in valid_days:
    print("open")
else:
    print("closed")