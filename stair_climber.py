'''
Unique Stair Climber
Given a number of stairs, return how many distinct ways someone can climb them taking either 1 or 2 steps at a time.
'''
def get_unique_climbs(steps):
    if steps <= 0:
        return 0
    elif steps == 1:
        return 1
    elif steps == 2:
        return 2
    
    # Use dynamic programming to store the number of ways to climb to each step
    dp = [0] * (steps + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, steps + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[steps]