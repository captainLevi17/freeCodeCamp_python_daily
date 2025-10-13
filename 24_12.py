'''
24 to 12
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
'''

def to_12(time):
    
    over_12 = ["13","14","15","16","17","18","19","20","21","22","23","24"]
    hr = time[0:2]
    period = "AM"
    if int(hr) > 12:
        period = "PM"
        hr = str(int(over_12.index(hr)) + 1)

    elif int(hr) < 10 and int(hr) > 0:
        hr = hr[1:2]
    elif hr == "11":
        hr = "11"
    else:
        hr = "12"
    return hr + ":"+ time[2:] + " " + period
