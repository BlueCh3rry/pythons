def check_temperature(temp_str):
    print("Testing temperature: ", temp_str)
    try:
        temp_str = int(temp_str)
    except ValueError:
        print("Error:", temp_str, "is not a valid number")
        return
    test_temperature_input(temp_str)


def test_temperature_input(x):
    if 40 < x:
        print("Error: ", x, "°C is too hot for plants (max 40°C)", sep="")
    elif x < 0:
        print("Error: ", x, " °C is too cold for plants (min 0°C)", sep="")
    else:
        print("Temperature ", x, " °C is perfect for plants!", sep="")


def main():
    print("=== Garden Temperature Checker ===\n")
    check_temperature(25)
    print()
    check_temperature("abc")
    print()
    check_temperature(100)
    print()
    check_temperature(-50)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
