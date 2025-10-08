def goldilocks_zone(mass):
    luminosity = mass ** 3.5
    start_zone = f"{((luminosity ** .5) * .95):.2f}"
    end_zone = f"{((luminosity ** .5) * 1.37):.2f}"

    return [start_zone, end_zone]

print(goldilocks_zone(1))
print(goldilocks_zone(0.5))