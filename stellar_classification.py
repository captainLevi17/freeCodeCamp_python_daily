#Stellar Classification based on surface temperature
def classification(temp):
    if temp >= 0 and temp <= 3699:
        return "M"
    elif temp >= 3700 and temp <= 5199:
        return "K"
    elif temp >= 5200 and temp <= 5999:
        return "G"
    elif temp >= 6000 and temp <= 7499:
        return "F"
    elif temp >= 7500 and temp <= 9999:
        return "A"
    elif temp >= 10000 and temp <= 29999:
        return "B"
    else: 
        return "O"
    