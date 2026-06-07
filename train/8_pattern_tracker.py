# DONE
def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        try:
            a, b = int(text[i]), int(text[i + 1])
            if a < b:
                count += 1
        except ValueError:
            pass
    return count


def main():
    test = pattern_tracker("112233")
    print(test)


main()
