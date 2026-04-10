def input_temperature(temp_str: str) -> int:
    val = int(temp_str)
    if val > 40:
        raise ValueError(f"{int(val)}°C is too cold for plants (max 40°C)")
    elif int(temp_str) < 0:
        raise ValueError(f"{int(temp_str)}°C is too cold for plants (min 0°C)")
    try:
        return int(temp_str)
    except ValueError:
        raise ValueError


def test_temperature() -> None:
    try:
        print("Input data is '25'")
        temp = input_temperature("25")
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    try:
        print("Input data is 'abc'")
        temp = input_temperature("abc")
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    try:
        print("Input data is '100'")
        temp = input_temperature("100")
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")
    try:
        print("Input data is '-50'")
        temp = input_temperature("-50")
        print(f"Temperature is now {temp}°C\n")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")


def main() -> None:
    print("=== Garden Temperature ===\n")
    test_temperature()


if __name__ == "__main__":
    main()
