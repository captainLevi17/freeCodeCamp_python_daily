'''
Acronym Finder
Given a string representing an acronym, return the full name of the organization it belongs to from the list below:

"National Avocado Storage Authority"
"Cats Infiltration Agency"
"Fluffy Beanbag Inspectors"
"Department Of Jelly"
"Wild Honey Organization"
"Eating Pancakes Administration"
Each letter in the given acronym should match the first letter of each word in the organization it belongs to, in the same order.
'''

def find_org(acronym):

    orgs = [
        "National Avocado Storage Authority",
        "Cats Infiltration Agency",
        "Fluffy Beanbag Inspectors",
        "Department Of Jelly",
        "Wild Honey Organization",
        "Eating Pancakes Administration"
    ]
    
    for org in orgs:
        words = org.split()
        print(words)
        if len(words) == len(acronym) and all(word[0].lower() == acronym[i].lower() for i, word in enumerate(words)):
            return org
    return "Organization not found"