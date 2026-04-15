def secure_archive(name: str, a: str, content: str) -> tuple[bool, str]:
    if a == 'r':
        try:
            with open(name, "r") as name_f:
                return (True, name_f.read())
        except IOError as e:
            return (False, str(e))

    elif a == 'w':
        try:
            with open(name, "w") as name_f:
                name_f.write(content)
            return (True, 'Content successfully written to file')
        except IOError as e:
            return (False, str(e))
    return (False, "")


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 'r', ""))

    print("\nUsing 'secure_archive' to read from an inaccessible file")
    print(secure_archive("/etc/master.passwd", 'r', ""))

    print("\nUsing 'secure_archive' to read from a regular file")
    print(secure_archive("ancient_fragment.txt", 'r', ""))

    print()
    print("Using 'secure_archive' to write previous content to a new file")
    print(secure_archive("ex4.txt", 'w', "ex4\nazd"))


if __name__ == "__main__":
    main()
