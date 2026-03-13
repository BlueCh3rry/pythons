import sys


def main():
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided.")
        return
    array = []
    for arg in sys.argv[1:]:
        array.append(int(arg))
    print("Total players:", len(sys.argv) - 1)
    print("Total score:", sum(array))
    print("Average score:", sum(array) / len(array))
    print("High score:", max(array))
    print("Low score:", min(array))
    print("Score range:", max(array) - min(array))
    print()


if __name__ == "__main__":
    main()
