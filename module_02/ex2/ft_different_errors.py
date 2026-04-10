def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("missing.txt")
    elif operation_number == 3:
        "Hello" + 7


def test_error_types() -> str:
    try:
        print("Testing operation 0...")
        garden_operations(0)
    except ValueError as e:
        print("Caught ValueError: ", e)
    try:
        print("Testing operation 1...")
        garden_operations(1)
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError: ", e)
    try:
        print("Testing operation 2...")
        garden_operations(2)
    except FileNotFoundError as e:
        print("Caught FileNotFoundError: ", e)
    try:
        print("Testing operation 3...")
        garden_operations(3)
    except TypeError as e:
        print("Caught TypeError: ", e)
    try:
        print("Testing operation 4...")
        garden_operations(0)
        garden_operations(1)
        garden_operations(2)
        garden_operations(3)
    except (ValueError, ZeroDivisionError, FileNotFoundError, TypeError):
        print("Operation completed successfully")
    return "\nAll error types tested successfully!"


def main() -> None:
    print("=== Garden Error Types Demo ===")
    print(test_error_types())


if __name__ == "__main__":
    main()
