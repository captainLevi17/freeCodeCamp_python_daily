def hex_to_decimal(hex):
    """Convert a hexadecimal string to a decimal integer."""
    hex = int(hex, 16)
    return hex

print(hex_to_decimal("2E"))
def decimal_to_hex(decimal):
    """Convert a decimal integer to a hexadecimal string."""
    decimal = hex(decimal)  #[2:].upper()
    return decimal

print(decimal_to_hex(46))