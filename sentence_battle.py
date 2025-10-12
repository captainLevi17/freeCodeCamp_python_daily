'''
Battle of Words
Given two sentences representing your team and an opposing team, where each word from your team battles the corresponding word from the opposing team, determine which team wins using the following rules:

The given sentences will always contain the same number of words.
Words are separated by a single space and will only contain letters.
The value of each word is the sum of its letters.
Letters a to z correspond to the values 1 through 26. For example, a is 1, and z is 26.
A capital letter doubles the value of the letter. For example, A is 2, and Z is 52.
Words battle in order: the first word of your team battles the first word of the opposing team, and so on.
A word wins if its value is greater than the opposing word's value.
The team with more winning words is the winner.
Return "We win" if your team is the winner, "We lose" if your team loses, and "Draw" if both teams have the same number of wins.
'''

def battle(our_team, opponent):

# letters a to z correspond to the values 1 through 26
# capital letter doubles the value of the letter
# words battle in order
# team with more winning words is the winner
# return "We win", "We lose", or "Draw"
    letters = "abcdefghijklmnopqrstuvwxyz"
    opponent_words = opponent.split(" ")
    our_words = our_team.split(" ")
    word_number = len(our_words)

    our_scores = []
    opponent_scores = []

    our_total = 0
    opponent_total = 0
# calculate scores for each word in both teams
    for words in our_words:
        score = 0
        for letter in words:
            multiplier = 1            
            if letter.isupper():
                multiplier = 2
                letter = letter.lower()
            score += (letters.index(letter) +1 ) * multiplier
        our_scores.append(score)

    for words in opponent_words:
        score = 0
        for letter in words:
            multiplier = 1            
            if letter.isupper():
                multiplier = 2
                letter = letter.lower()
            score += (letters.index(letter) +1 ) * multiplier
        opponent_scores.append(score)
# compare scores and determine winner
    for i in range(word_number):
        if our_scores[i] > opponent_scores[i]:
            our_total += 1
        elif our_scores[i] == opponent_scores[i]:
            continue
        else:
            opponent_total += 1
# determine overall winner
    if our_total > opponent_total:
        return "We win"
    elif our_total == opponent_total:
        return "Draw"
    else:
        return "We lose"

