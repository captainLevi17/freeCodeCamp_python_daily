'''
Allergen Friendly Meals
Given an array of meals and an array of allergens to avoid, return the names of all the meals that contain none of the given allergens.

Each meal is in the format [meal, allergens], where meal is the name of the meal, and allergens is an array of the allergens the meal contains. For example, ["pasta", ["wheat", "milk"]].
Allergens to avoid will be an array of strings.
Return safe meal names in the same order given. If no meal is safe, return an empty array.


'''

def get_allergen_friendly_meals(meals, allergens):
    safe_meals = []
    
    for meal, meal_allergens in meals:
        if not any(allergen in meal_allergens for allergen in allergens):
            safe_meals.append(meal)
    
    return safe_meals