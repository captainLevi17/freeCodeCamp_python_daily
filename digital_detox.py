'''
Digital Detox
Given an array of your login logs, determine whether you have met your digital detox goal.

Each log is a string in the format "YYYY-MM-DD HH:mm:ss".

You have met your digital detox goal if both of the following statements are true:

You logged in no more than once within any four-hour period.
You logged in no more than 2 times on any single day.
'''
from datetime import datetime, timedelta

# Use `datetime` to parse timestamp strings and `timedelta` for time comparisons


def digital_detox(logs):
    # Parse each timestamp string into a datetime object
    dts = [datetime.strptime(s, "%Y-%m-%d %H:%M:%S") for s in logs]

    # Sort timestamps so adjacent items are the closest in time
    dts.sort()

    # Count logins per calendar day and enforce the "no more than 2 per day" rule
    counts = {}
    for dt in dts:
        day = dt.date()
        counts[day] = counts.get(day, 0) + 1
        if counts[day] > 2:
            return False

    # Ensure no two consecutive logins are less than 4 hours apart
    for i in range(len(dts) - 1):
        if dts[i + 1] - dts[i] < timedelta(hours=4):
            return False

    # Passed both checks
    return True

'''
digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]) should return False.
'''