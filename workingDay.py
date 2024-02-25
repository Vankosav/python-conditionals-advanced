day = str(input())

workingDay = {
    "Monday": "Working day",
    "Tuesday": "Working day",
    "Wednesday": "Working day",
    "Thursday": "Working day",
    "Friday": "Working day",
    "Saturday": "Weekend",
    "Sunday": "Weekend",
}

print(workingDay.get(day, "Error"))

