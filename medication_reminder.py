'''
Medication Reminder
Given an array of medications and a string representing the current time, return the next medication you need to take and how long until you need to take it.

Each medication is in the format [name, lastTaken], where name is the name of the medication and lastTaken is the time it was last taken.
All given times will be in "HH:MM" (24-hour) format.
Use the following medication schedule:

Name	Schedule
Deployxitrin	08:00, 16:00
Debuggamanizole	07:00, 13:00, 21:00
Mergeflictamine	every 4 hours
Return a string in the format "{name} in Hh Mm". For example, "Debuggamanizole in 2h 0m" or "Deployxitrin in 1h 5m".

'''

def medication_reminder(medications, current_time):
    schedule = {
        "Deployxitrin": ["08:00", "16:00"],
        "Debuggamanizole": ["07:00", "13:00", "21:00"],
    }
    
    def time_to_minutes(t):
        h, m = map(int, t.split(':'))
        return h * 60 + m
    
    current_minutes = time_to_minutes(current_time)
    candidates = []
    
    for name, last_taken in medications:
        if name == "Mergeflictamine":
            # Every 4 hours from last_taken
            last_taken_minutes = time_to_minutes(last_taken)
            next_time = last_taken_minutes
            # Find next occurrence after current time
            while next_time <= current_minutes:
                next_time += 4 * 60
            # Handle 24-hour wrap-around
            next_time = next_time % (24 * 60)
            if next_time <= current_minutes:
                next_time += 24 * 60
            time_until = next_time - current_minutes
            candidates.append((time_until, name))
        elif name in schedule:
            # Fixed schedule
            for scheduled_time in schedule[name]:
                scheduled_minutes = time_to_minutes(scheduled_time)
                if scheduled_minutes > current_minutes:
                    # Time is later today
                    time_until = scheduled_minutes - current_minutes
                    candidates.append((time_until, name))
                else:
                    # Time has passed, next occurrence is tomorrow
                    time_until = (24 * 60 - current_minutes) + scheduled_minutes
                    candidates.append((time_until, name))
    
    # Find medication with minimum time until next dose
    min_time_until, next_medication = min(candidates)
    hours = min_time_until // 60
    minutes = min_time_until % 60
    return f"{next_medication} in {hours}h {minutes}m"
