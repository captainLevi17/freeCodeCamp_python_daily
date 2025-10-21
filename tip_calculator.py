'''
Tip Calculator
Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

Prices will be given in the format: "$N.NN".
Custom tip percents will be given in this format: "25%".
Return amounts in the same "$N.NN" format, rounded to two decimal places.
For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].
'''
def calculate_tips(meal_price, custom_tip):
    value = float(meal_price[1:])
    tips = []
    fifteen_percent = value * .15
    twenty_percent = value * .20
    custom_tip = int(custom_tip[:-1]) * .01
    custom_percent = value * custom_tip
    tips.append(f"${fifteen_percent:.2f}")
    tips.append(f"${twenty_percent:.2f}")
    tips.append(f"${custom_percent:.2f}")

    return tips

print(calculate_tips("$10.00", "25%"))

'''
Extract the meal price
Create empty list
calculate 15%
append to list
calculate 25%
append to list
calculate custom tip
append to list
return list
'''