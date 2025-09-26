def speeding(speeds, limit):
    speedy_cars = []
    for car in speeds:
        if car > limit:
            speedy_cars.append(car)
    if len(speedy_cars) == 0:
        return [0,0]
    overspeed_count = 0
    for car in speedy_cars:
        amount = car - limit
        overspeed_count += amount
    average_amount = overspeed_count/len(speedy_cars)
    print(speedy_cars)
    
    return [len(speedy_cars), average_amount]