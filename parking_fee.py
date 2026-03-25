'''
Parking Fee Calculator
Given two strings representing the time you parked your car and the time you picked it up, calculate the parking fee.

The given strings will be in the format "HH:MM" using a 24-hour clock. So "14:00" is 2pm for example.
The first string will be the time you parked your car, and the second will be the time you picked it up.
If the pickup time is earlier than the entry time, it means the parking spanned past midnight into the next day.
Fee rules:

Each hour parked costs $3.
Partial hours are rounded up to the next full hour.
If the parking spans overnight (past midnight), an additional $10 overnight fee is applied.
There is a minimum fee of $5 (only used if the total would be less than $5).
Return the total cost in the format "$cost", "$5" for example.

'''

def calculate_parking_fee(park_time, pickup_time):
    from datetime import datetime, timedelta
    fmt = "%H:%M"
    park_dt = datetime.strptime(park_time, fmt)
    pickup_dt = datetime.strptime(pickup_time, fmt)
    if pickup_dt < park_dt:
        pickup_dt += timedelta(days=1)
    total_hours = (pickup_dt - park_dt).total_seconds() / 3600
    fee = 3 * (int(total_hours) + (1 if total_hours % 1 > 0 else 0))
    if pickup_dt.day != park_dt.day:
        fee += 10
    return f"${max(fee, 5)}"
