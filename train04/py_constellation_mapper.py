"""

"
Allowed functions: None. Use only permitted built-in functions
to avoid getting 0 on exam day.
"

Write a function that maps a constellation of stars onto a grid and
returns the visual representation as a list of strings.

The function should:
- Take a list of star coordinates as tuples (row, col) and grid size as integer
- Return a list of strings representing the grid
- Stars are represented by '*' and empty spaces by '.'
- Grid coordinates start from (0, 0) at top-left
- Ignore coordinates outside the grid boundaries
- Handle duplicate coordinates (star appears only once)

constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)
-> ['*..', '.*.', '..*']

constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)
-> ['.*.', '***', '.*.']

constellation_mapper([], 2)
-> ['..', '..']

constellation_mapper([(0, 0), (0, 0), (1, 1)], 2)
-> ['*.', '.*']

constellation_mapper([(0, 0), (5, 5)], 3)
-> ['*..', '...', '...']

constellation_mapper([(1, 0), (1, 1), (1, 2)], 3)
-> ['...', '***', '...']

"""


def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    pattern = "." * dim
    res_lst = []
    for _ in range(dim):
        res_lst.append(pattern)
    cpy_lst = res_lst
    for row, col in stars:
        if row > len(pattern) or row > len(res_lst):
            return cpy_lst
        char = list(res_lst[row])
        char[col] = "*"
        res_lst[row] = "".join(char)
    return res_lst


def main():
    print("1", constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
    print("2",
          constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
    print("3", constellation_mapper([], 2))
    print("4", constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))
    print("5", constellation_mapper([(0, 0), (5, 5)], 3))
    print("6", constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))


if __name__ == "__main__":
    main()
