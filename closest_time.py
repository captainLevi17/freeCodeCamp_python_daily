'''
Closest Time Direction
Given two times, determine whether you can get from the first to the second faster by moving forward or backward.

Times are given in 24-hour format ("HH:MM")
The clock wraps around (23:59 goes to 00:00 when moving forward, and 00:00 goes to 23:59 when moving backwards)
Return:

"forward" if moving forward is shorter
"backward" if moving backward is shorter
"equal" if both directions take the same amount of time
'''
def get_direction(time1, time2):
    def time_to_minutes(time):
        hours, minutes = map(int, time.split(':'))
        return hours * 60 + minutes
    
    t1 = time_to_minutes(time1)
    t2 = time_to_minutes(time2)
    
    forward_time = (t2 - t1) % (24 * 60)
    backward_time = (t1 - t2) % (24 * 60)
    
    if forward_time < backward_time:
        return "forward"
    elif backward_time < forward_time:
        return "backward"
    else:
        return "equal"