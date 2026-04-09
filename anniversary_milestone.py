'''
Anniversary Milestones
Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:

Years Married	Milestone
1	"Paper"
5	"Wood"
10	"Tin"
25	"Silver"
40	"Ruby"
50	"Gold"
60	"Diamond"
70	"Platinum"
If they haven't reached the first milestone, return "Newlyweds".

'''

def get_milestone(years):
    milestones = {
        1: "Paper",
        5: "Wood",
        10: "Tin",
        25: "Silver",
        40: "Ruby",
        50: "Gold",
        60: "Diamond",
        70: "Platinum"
    }
    if years < 1:
        return "Newlyweds"
    for milestone_year in sorted(milestones.keys(), reverse=True):
        if years >= milestone_year:
            return milestones[milestone_year]
