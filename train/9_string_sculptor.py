# DONE
def string_sculptor(text: str) -> str:
    if not text:
        return text
    res = ""
    count_let = 0
    for txt in text:
        if txt.isalpha():
            count_let += 1
            if count_let % 2 == 0:
                res += txt.upper()
            else:
                res += txt.lower()
        else:
            res += txt
    return res


def main():
    test = string_sculptor("Python3.9!")
    print(test)


main()
