import sys


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 2:
        print(f"Accessing file: '{sys.argv[1]}'")
        try:
            file = open(sys.argv[1], "r")
            print("---\n")
            print(file.read())
            file.close()
            print(f"\n---\nFile '{file.name}' closed.")
        except IOError as e:
            print(f"Error opening file {file}: {e}")
            return
    else:
        print("Usage: ft_ancient_text.py <file>")
        return


if __name__ == "__main__":
    main()
