def input_temperature(temp_str: str) -> str:
    print(f"\nInput data is '{temp_str}'")
    val = int(temp_str)
    if val > 40:
        raise ValueError(f"{int(val)}°C is too cold for plants (max 40°C)")
    elif int(temp_str) < 0:
        raise ValueError(f"{int(temp_str)}°C is too cold for plants (min 0°C)")
    try:
        return f"Temperature is now {int(temp_str)}°C"
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
    try:
        print(input_temperature("100"))
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    try:
        print(input_temperature("-50"))
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===")
    test_temperature()


if __name__ == "__main__":
    main()

