# DONE
def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    for lst in matrix:
        lst.reverse()
    return matrix


def main():
    test = mirror_matrix([[1, 2], [3, 4], [5, 6]])
    print(test)


main()
