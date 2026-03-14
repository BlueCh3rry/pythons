def check_temperature(temp_str: str) -> str:
    print("Testing temperature: ", temp_str)
    try:
        temp_str = int(temp_str)
    except ValueError:
        return f"Error: {temp_str} is not a valid number"
    return test_temperature_input(temp_str)


def test_temperature_input(x: int) -> str:
    if 40 < x:
        return f"Error: {x}°C is too hot for plants (max 40°C)"
    elif x < 0:
        return f"Error: {x}°C is too cold for plants (min 0°C)"
    else:
        return f"Temperature {x}°C is perfect for plants!"


def main() -> None:
    print("=== Garden Temperature Checker ===\n")
    print(check_temperature(25))
    print()
    print(check_temperature("abc"))
    print()
    print(check_temperature(100))
    print()
    print(check_temperature(-50))
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
