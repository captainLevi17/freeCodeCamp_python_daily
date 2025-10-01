def to_decimal(binary):
    counter = 0
    container = []
    for n in binary[::-1]:
        container.append(int(n) * (2 ** counter))
        counter += 1
    return sum(container)