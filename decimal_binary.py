def to_binary(decimal):
    container = []
    while True:
        if decimal == 0:
            break
        else:
            remainder = decimal % 2
            decimal = decimal // 2
            if remainder == 0:
                container.append("0")
            else:
                container.append("1")

    return "".join(container[::-1])

print(to_binary(12))