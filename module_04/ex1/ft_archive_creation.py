import sys


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) == 2:
        print(f"Accessing file: '{sys.argv[1]}'\n---\n")
        try:
            with open(sys.argv[1], "r") as file:
                content = []
                for line in file:
                    print(line.rstrip("\n"))
                    content.append(line)
            print(f"\n---\nFile '{file.name}' closed.\n")
        except IOError as e:
            print(f"Error opening file {sys.argv[1]}: {e}")
            return

        transformed = []
        print("Transform data:\n---\n")
        for line in content:
            nline = line.rstrip("\n") + "#\n"
            print(nline.rstrip("\n"))
            transformed.append(nline)
        print("\n---")
        save_file = input("Enter new file name (or empty):")
        if save_file:
            with open(save_file, "w") as file_save:
                print(f"Saving data to '{file_save.name}'")
                for line in transformed:
                    file_save.write(line)
            print(f"Data saved in file '{file_save.name}'")
        else:
            print("Not saving data")
    else:
        print("Usage: ft_ancient_text.py <file>")
        return


if __name__ == "__main__":
    main()
