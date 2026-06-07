# DONE
def ByAscii(s) -> int:
    res = 0
    c: str
    for c in s:
        if c.isalpha() and (c == c.upper()):
            res += ord(c) + 32
        else:
            res += ord(c)
    return res


def same_len(s: list[str]) -> bool:
    for txt in s:
        for other in s:
            if len(txt) == len(other):
                return True
    return False


def cryptic_sorter(strings: list[str]) -> list[str]:
    if len(strings) < 2 or not strings:
        return strings
    cpy_str = strings.copy()
    cpy_str.sort(key=lambda s: len(s))
    asc_lst = []
    res_lst = []
    if len(cpy_str) > 1 and same_len(strings):
        len_count = 1
        while len_count <= len(cpy_str[(len(cpy_str)) - 1]):
            for curr in range(0, len(cpy_str)):
                if len(cpy_str[curr]) == len_count:
                    asc_lst.append(cpy_str[curr])
            asc_lst.sort(key=ByAscii)
            res_lst.extend(asc_lst)
            asc_lst.clear()
            len_count += 1
    return res_lst


def main():
    s = ["aaa", "bbb", "AAA", "BBB"]
    t = ["apple", "cat", "banana", "dog", "elephant"]

    print(cryptic_sorter(["hello", "world", "hi", "test"]))
    print(cryptic_sorter([""]))
    print(cryptic_sorter(s))
    print(cryptic_sorter(t))


main()
