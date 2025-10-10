'''
Space Week Day 6: Moon Phase
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" 
and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

"New": days 1 - 7
"Waxing": days 8 - 14
"Full": days 15 - 21
"Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.

Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
You will not be given any dates before the reference date.
Return the correct phase as a string.

How to solve:
1. Parse the input date string to extract year, month, and day.
2. Calculate the total number of days between the reference date (2000-01-06) and the input date.
3. Determine the day in the lunar cycle by taking the total days modulo 28.
4. Map the day in the lunar cycle to the corresponding moon phase:
   - Days 1-7: "New"
   - Days 8-14: "Waxing"
   - Days 15-21: "Full"
   - Days 22-28: "Waning"

'''

def moon_phase(date_string):
    # parse date and calculate days since reference date
    import datetime
    date = date_string.split("-")
    y = int(date[0])
    m = int(date[1])
    d = int(date[2])
    ref = datetime.date(2000, 1, 6)
    target = datetime.date(y, m, d)
    days = (target - ref).days
    lunar_day =  (days % 28) 
    print(lunar_day)
    if lunar_day < 7:
        date_string = "New"
    elif lunar_day < 14:
        date_string = "Waxing"
    elif lunar_day < 21:
        date_string = "Full"
    else:
        date_string = "Waning"
    return date_string
import datetime
tday = datetime.date.today()
bday = datetime.date(1996, 10, 17)

y = (tday.month - bday.month)
print(y)