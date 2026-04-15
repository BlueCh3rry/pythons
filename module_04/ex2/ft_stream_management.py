import sys


def main() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")

    if len(sys.argv) == 2:
        print(f"Accessing file: '{sys.argv[1]}' ---\n")
        try:
            with open(sys.argv[1], "r") as file:
                content = []
                for line in file:
                    print(line.rstrip("\n"))
                    content.append(line)
            print(f"\n---\nFile '{file.name}' closed.\n")
        except IOError as e:
            f_name = sys.argv[1]
            sys.stderr.write(f"[STDERR] Error opening file '{f_name}': {e}\n")
            return

        transformed = []
        print("Transform data:\n---\n")
        for line in content:
            nline = line.rstrip("\n") + "#\n"
            print(nline.rstrip("\n"))
            transformed.append(nline)
        print("\n---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()

        save_file = sys.stdin.readline().rstrip("\n")
        if save_file:
            print(f"Saving data to '{save_file}'")
            try:
                with open(save_file, "w") as file_save:
                    for line in transformed:
                        file_save.write(line)
            except IOError as e:
                f_name = sys.argv[1]
                sys.stderr.write(f"[STDERR] Error opening file '{f_name}': {e}\n")
                print("Data not saved")
            else:
                print(f"Data saved in file '{file_save.name}'")
        else:
            print("Not saving data")
    else:
        print("Usage: ft_ancient_text.py <file>")
        return


if __name__ == "__main__":
    main()
