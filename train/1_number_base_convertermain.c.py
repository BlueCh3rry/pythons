# DONE
def give_base(base_nbr: int) -> str:
    return "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base_nbr]


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if number is None:
        return "ERROR"

    try:
        val = int(number, from_base)
        if val == 0:
            return "0"
    except ValueError:
        return "ERROR"

    try:
        digits = give_base(to_base)
    except ValueError:
        return "ERROR"
    res = ""
    while val > 0:
        res = digits[val % to_base] + res
        val //= to_base
    return res


def main():
    test = number_base_converter("123", 10, 42)
    print(test)


main()
