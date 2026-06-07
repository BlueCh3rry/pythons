# DONE
def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    list1.extend(list2)
    list1.sort()
    return list1


def main():
    test = shadow_merge([1, 2, 3], [4, 5, 6])
    print(test)


main()
