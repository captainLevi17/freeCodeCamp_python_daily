'''
What Day Is It?
Given a Unix timestamp in milliseconds, return the day of the week.

Valid return days are:

"Sunday"
"Monday"
"Tuesday"
"Wednesday"
"Thursday"
"Friday"
"Saturday"
Be sure to ignore time zones.

'''
from datetime import datetime

def get_day_of_week(timestamp):
    return datetime.utcfromtimestamp(timestamp / 1000).strftime("%A")
