import sys


def main() -> None:
    inside_venv = sys.prefix != sys.base_prefix
    print()
    if inside_venv is False:
        print("MATRIX STATUS: You're still plugged in")
        print("\nCurrent Python: None detected")
    else:
        print("MATRIX STATUS: Welcome to the construc")
        print("\nCurrent Python:", sys.prefix)

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\Scripts\activate # On Windows")
    print("Then run this program again")

if __name__ == "__main__":
    main()
