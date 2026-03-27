'''
Equinox Shadows
Today is the equinox, when the sun is directly above the equator and perfectly overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.

The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
You will only be given a time in 30 minute increments.
Rules:

The sun rises at 6am directly "east", and sets at 6pm directly "west".
A shadow always points opposite the sun.
The shadow's length (in feet) is the number of hours away from noon, cubed.
There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.
Return:

If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
Otherwise, return "No shadow".
For example, given "10:00", return "8ft west" because 10am is 2 hours from noon, so 2 cubed = 8 feet, and the shadow points west because the sun is in the east at 10am.

'''
def get_shadow(time):
    hours, minutes = map(int, time.split(':'))
    total_hours = hours + minutes / 60
    print(minutes)
    
    if total_hours < 6 or total_hours >= 18:
        return "No shadow"
    
    hours_from_noon = abs(total_hours - 12)
    print(hours_from_noon)
    
    if hours_from_noon == 0:
        return "No shadow"
    
    shadow_length = float(hours_from_noon ** 3)
    
    if total_hours < 12:
        direction = "west"
    else:
        direction = "east"
    
    return f"{shadow_length}ft {direction}"

print(get_shadow("10:00"))
print(get_shadow("17:30"))