def garden_operations(x):
    if x == "value":
        int("abc")
    elif x == "zero":
        10 / 0
    elif x == "file":
        open("missing.txt")
    elif x == "key":
        plants = {"rose": 3}
        print(plants["missing_plant"])


def test_error_types():
    try:
        print("Testing ValueError...")
        garden_operations("value")
    except ValueError as e:
        print("Caught ValueError: ", e)
    try:
        print("\nTesting ZeroDivisionError...")
        garden_operations("zero")
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError: ", e)
    try:
        print("\nTesting FileNotFoundError...")
        garden_operations("file")
    except FileNotFoundError as e:
        print("Caught FileNotFoundError: ", e)
    try:
        print("\nTesting KeyError...")
        garden_operations("key")
    except KeyError as e:
        print("Caught KeyError: ", e)
    try:
        print("\nTesting multiple errors together...")
        garden_operations("key")
        garden_operations("file")
        garden_operations("zero")
        garden_operations("value")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


def main():
    print("=== Garden Error Types Demo ===\n")
    test_error_types()


if __name__ == "__main__":
    main()