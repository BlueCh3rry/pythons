"""

"
Forbidden built-ins / modules: sorted(), .sort(), heapq.merge().
Use only permitted built-in functions to avoid getting 0 on exam day.
"

Write a function that merges multiple sorted lists into one sorted list
while maintaining the sort order efficiently.

The function should:
- Take a list of sorted integer lists as input
- Return a single merged list in ascending order
- Preserve all duplicate elements in the final result
- Handle empty lists and empty input gracefully
- Maintain optimal efficiency for large inputs

Rules:
- All input lists are guaranteed to be sorted in ascending order
- Empty lists should be ignored during merging
- Return empty list if no valid input is provided
- Preserve duplicates across different lists
- Handle negative numbers correctly

Edge cases to handle:
- Empty input list: return empty list
- Lists containing only empty lists: return empty list
- Single list input: return copy of that list
- All duplicate elements: preserve all instances
- Negative numbers: handle correctly in sort order

merge_sorted_lists([[1, 3, 5], [2, 4, 6]])
-> [1, 2, 3, 4, 5, 6]

merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]])
-> [1, 2, 3, 4, 5, 6, 7, 8, 9]

merge_sorted_lists([[5], [1, 3], [2, 4]])
-> [1, 2, 3, 4, 5]

merge_sorted_lists([[1, 1, 2], [2, 3, 3]])
-> [1, 1, 2, 2, 3, 3]

merge_sorted_lists([[], [1, 2, 3]])
-> [1, 2, 3]

merge_sorted_lists([[]])
-> []

merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]])
-> [-5, -3, -1, 0, 2, 4]

merge_sorted_lists([[10], [10], [10]])
-> [10, 10, 10]

"""


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    res_lst = []
    for list in lists:
        for elem in list:
            res_lst.append(elem)
    for i in range(len(res_lst)):
        for j in range(len(res_lst)):
            if res_lst[i] <= res_lst[j]:
                tmp = res_lst[i]
                res_lst[i] = res_lst[j]
                res_lst[j] = tmp
    return res_lst


def main():
    print("1", merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))
    print("2", merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))
    print("3", merge_sorted_lists([[5], [1, 3], [2, 4]]))
    print("4", merge_sorted_lists([[1, 1, 2], [2, 3, 3]]))
    print("5", merge_sorted_lists([[], [1, 2, 3]]))
    print("6", merge_sorted_lists([[]]))
    print("7", merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))
    print("8", merge_sorted_lists([[10], [10], [10]]))


if __name__ == "__main__":
    main()
