# DONE
def give_base(base_nbr: int) -> str:
    return "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:base_nbr]


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if number is None:
        return "ERROR"
    val = int(number, from_base)
    if val == 0:
        return "0"

    digits = give_base(to_base)
    res = ""
    while val > 0:
        res = digits[val % to_base] + res
        val //= to_base
    return res


def main():
    test = number_base_converter("1010", 2, 10)
    print(test)


main()
