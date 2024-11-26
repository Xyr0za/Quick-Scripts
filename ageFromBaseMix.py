import itertools

perms = list(itertools.permutations(range(1,7)))

def map_elements(arr):
    return arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]


def base_to_decimal(number, base):
    if base == 1:
        return number
    number = str(number)
    """Convert a number from a given base to decimal."""
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    if base > len(digits) or base < 2:
        raise ValueError("Base must be between 2 and 36")

    decimal_value = 0
    for digit in number:
        decimal_value = decimal_value * base + digits.index(digit)

    return decimal_value

for set in perms:
    a, b, c, d, e, f = map_elements(set)

    num1 = f"{c}{a}{b}"
    b1 = e

    num2 = f"{a}{b}{c}"
    b2 = d

    num3 = f"{b}{c}{a}"
    b3 = f

    d1 = int(base_to_decimal(num1, b1))
    d2 = int(base_to_decimal(num2, b2))
    d3 = int(base_to_decimal(num3, b3))

    if d1 + 1 == d2 and d2 + 1 == d3:
        print(d1,d2,d3)
