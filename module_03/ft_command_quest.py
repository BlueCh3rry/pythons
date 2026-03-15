import sys


def main() -> None:
    print("=== Command Quest ===")
    if len(sys.argv) == 1:
        print("No arguments provided!")
    print("Program name:", sys.argv[0])
    print("Total arguments:", len(sys.argv) - 1)
    count = 0
    for arg in sys.argv[1:]:
        count += 1
        print("Argument", count, ":", arg)
    print("Total arguments:", len(sys.argv))
    print()


if __name__ == "__main__":
    main()
