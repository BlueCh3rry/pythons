# DONE
def echo_validator(text: str) -> bool:
    if not text:
        return False
    new_txt = text.replace(" ", "").lower()
    print(new_txt)
    if not new_txt:
        return False
    part1 = new_txt[:int(len(new_txt)/2)]
    print(part1)
    if len(new_txt) % 2 == 0:
        temp_p2 = new_txt[int(len(new_txt)/2):]
    else:
        temp_p2 = new_txt[int(len(new_txt)/2) + 1:]
    part2 = temp_p2[::-1]
    print(part2)
    if part1 == part2:
        return True
    return False


def main():
    test = echo_validator(" .r wr. ")
    print(test)


main()
