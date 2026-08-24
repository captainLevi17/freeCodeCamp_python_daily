'''
Mile Pace
Given a number of miles ran, and a time in "MM:SS" (minutes:seconds) it took to run those miles, return a string for the average time it took to run each mile in the format "MM:SS".

Add leading zeros when needed.
'''

def mile_pace(miles, duration):
    # Split the duration into minutes and seconds
    minutes, seconds = map(int, duration.split(':'))
    
    # Convert total time to seconds
    total_seconds = minutes * 60 + seconds
    
    # Calculate average time per mile in seconds
    average_seconds_per_mile = total_seconds / miles
    
    # Convert back to minutes and seconds
    avg_minutes = int(average_seconds_per_mile // 60)
    avg_seconds = int(average_seconds_per_mile % 60)
    
    # Format the result with leading zeros
    return f"{avg_minutes:02}:{avg_seconds:02}"