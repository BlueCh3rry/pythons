"""

"
Allowed functions: None. Use only permitted built-in functions
to avoid getting 0 on exam day.
"

Write a function that finds the intersection of multiple sorted lists.
Return a new list containing elements that appear in ALL input lists,
in sorted order.

The function should:
- Return elements that appear in ALL lists
- Result should be sorted in ascending order
- Remove duplicates from the result
- Handle empty input or empty lists gracefully
- If any list is empty, the intersection is empty


list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]])
-> [2, 3]

list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]])
-> [4]

list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]])
-> [1, 2, 3]

list_intersection_finder([[1, 2, 3], [4, 5, 6]])
-> []

list_intersection_finder([])
-> []

list_intersection_finder([[1, 2, 3], []])
-> []

list_intersection_finder([[5]])
-> [5]

"""


def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    val_match = []
    if not lists:
        return []
    if len(lists) == 1:
        return lists[0]
    val_ref = lists[0]
    for i in range(1, len(lists)):
        for val in lists[i]:
            if val not in val_ref:
                continue
            else:
                val_match.append(val)
    if not val_match:
        return []
    res_lst = []
    for i in range(len(val_match)):
        count = 0
        j = i+1
        for j in range(i, len(val_match)):
            if val_match[i] == val_match[j]:
                count += 1
            j += 1
        if count == len(lists)-1:
            res_lst.append(val_match[i])
    return res_lst


def main():
    print("1", list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
    print("2",
          list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))
    print("3",
          list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))
    print("4", list_intersection_finder([[1, 2, 3], [4, 5, 6]]))
    print("5", list_intersection_finder([]))
    print("6", list_intersection_finder([[1, 2, 3], []]))
    print("7", list_intersection_finder([[5]]))


if __name__ == "__main__":
    main()
