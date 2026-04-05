def input_temperature(temp_str: str) -> str:
    print(f"Input data is '{temp_str}'")
    try:
        return f"Temperature is now {int(temp_str)}°C\n"
    except ValueError:
        raise ValueError


def test_temperature() -> None:
    try:
        print(input_temperature("25"))
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        print(input_temperature("abc"))
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
