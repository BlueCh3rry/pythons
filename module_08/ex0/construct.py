import sys


def main() -> None:
    inside_venv = sys.prefix != sys.base_prefix
    print()
    if inside_venv is False:
        print("MATRIX STATUS: You're still plugged in")
        print("\nCurrent Python: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again")
    else:
        print("MATRIX STATUS: Welcome to the construc")
        print("\nCurrent Python:", sys.prefix)
        print("Virtual Environment:", sys.base_prefix)
        print("Environment Path:", sys.base_prefix)
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:")
        print(path)


if __name__ == "__main__":
    main()
