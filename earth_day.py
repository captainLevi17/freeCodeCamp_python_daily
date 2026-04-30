'''
Earth Day Cleanup Crew
Today is Earth Day. Given an array of items you cleaned up, return your total cleanup score based on the rules below.

Given items will be one of:

Item	Base Value
"bottle"	10
"can"	6
"bag"	8
"tire"	35
"straw"	4
"cardboard"	3
"newspaper"	3
"shoe"	12
"electronics"	25
"battery"	18
"mattress"	38
A Rare item is represented as ["rare", value]. For example, ["rare", 80]. Rare items do not get a streak bonus.

Streak bonus: If the same item appears consecutively, it gets increasing bonus points.

First consecutive occurrence: base value
Second: base value + 1
Third: base value + 2
etc.
Fifth Item Multiplier: Every fifth item collected gets a multiplier.

Fifth item: *2
Tenth item: *3
etc.
Apply the multiplier after calculating any bonuses.

'''

def get_cleanup_score(items):
    score = 0
    item_values = {
        "bottle": 10,
        "can": 6,
        "bag": 8,
        "tire": 35,
        "straw": 4,
        "cardboard": 3,
        "newspaper": 3,
        "shoe": 12,
        "electronics": 25,
        "battery": 18,
        "mattress": 38
    }
    last_item = None
    consecutive_count = 0
    for i, item in enumerate(items):
        if isinstance(item, list) and item[0] == "rare":
            score += item[1]
            last_item = None
            consecutive_count = 0
            continue
        
        # Track consecutive occurrences
        if item == last_item:
            consecutive_count += 1
        else:
            consecutive_count = 1
            last_item = item
        
        base_value = item_values.get(item, 0)
        bonus = consecutive_count - 1
        total_value = base_value + bonus
        
        # Apply multiplier only to every 5th item (positions 5, 10, 15, etc.)
        position = i + 1
        if position % 5 == 0:
            multiplier = (position // 5) + 1
        else:
            multiplier = 1
        
        score += total_value * multiplier
    return score