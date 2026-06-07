# DONE
def string_permutation_checker(s1: str, s2: str) -> bool:
    t1 = "".join(sorted(s1)).replace(" ", "")
    print(t1)
    t2 = "".join(sorted(s2)).replace(" ", "")
    print(t2)
    if t1 == t2:
        return True
    return False


def main():
    test = string_permutation_checker("a gentleman", "elegant man")
    print(test)


main()
