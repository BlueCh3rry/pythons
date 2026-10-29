"""

"
FORBIDDEN built-ins / modules: collections.deque.rotate(). Use only permitted built-in functions to avoid getting 0 on exam day.
"

Write a Python function that takes two lists (arrays) as parameters and determines if the second list is a rotation of the first list (left or right).

A rotation means that the elements are shifted circularly. For example, shifting [1, 2, 3] to the right by one position results in [3, 1, 2].

The function must return True if arr2 is a rotation of arr1, and False otherwise.
If the arrays have different lengths, they cannot be rotations of each other.
Two empty arrays are considered rotations of each other.


array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3])
-> True

array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])
-> True

array_rotation_detector([1, 2, 3], [3, 2, 1])
-> False

array_rotation_detector([1, 2], [1, 2, 3])
-> False

array_rotation_detector([], [])
-> True

"""

def array_rotation_detector(arr1: list, arr2: list) -> bool:
    i = 0
    j = 0
    if not arr1 and not arr2:
        return True
    elif not arr1 or not arr2:
        return False
    elif len(arr1) < len(arr2):
        return False
    while arr1[i] != arr2[j]:
        if j == len(arr2):
            return False
        j += 1
    while i < len(arr1):
        if j == len(arr2):
            j = 0
        if arr1[i] != arr2[j]:
            return False
        i += 1
        j += 1
    return True

def main():
    print("1", array_rotation_detector([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
    print("2", array_rotation_detector([1, 2, 3, 4, 5], [5, 1, 2, 3, 4])) 
    print("3", array_rotation_detector([1, 2, 3], [3, 2, 1])) 
    print("4",array_rotation_detector([1, 2], [1, 2, 3])) 
    print("5",array_rotation_detector([], []))

if __name__ == "__main__":
    main()