# DONE
def twist_it(arr: list[int], k: int) -> list[int]:
    t1 = arr[(len(arr) - k):]
    print(t1)
    t2 = arr[:(len(arr) - k)]
    print(t2)
    t1.extend(t2)
    return t1


def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr or k < 1 or k == len(arr):
        return arr
    if len(arr) > k:
        new_arr = twist_it(arr, k)
    else:
        new_k = k % len(arr)
        new_arr = twist_it(arr, new_k)
    return new_arr


def main():
    test = twist_sequence([1, 2, 3, 4], 4)
    print(test)


main()
