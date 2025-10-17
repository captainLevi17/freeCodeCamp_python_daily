def mask(card):

    if "-" in card:
        card = card.split('-')
        last_digits = card[-1]
        masked_numbers = []
        for i in range(3):
            masked_numbers.append("****")
        masked_numbers.append(last_digits)
        return "-".join(masked_numbers)
    else:
        card = card.split(" ")
        last_digits = card[-1]
        masked_numbers = []
        for i in range(3):
            masked_numbers.append("****")
        masked_numbers.append(last_digits)
        return " ".join(masked_numbers)
