def check_plant_health(name, level, hours):
    if not name:
        raise ValueError("Plant name cannot be empty!")
    if level < 1:
        raise ValueError(f"Water level {level} is too low (min 1)")
    elif level > 10:
        raise ValueError(f"Water level {level} is too high (max 10)")
    if hours < 2:
        raise ValueError(f"Sunlight hours {hours} is too low (min 2)")
    elif hours > 12:
        raise ValueError(f"Sunlight hours {hours} is too high (max 12)")
    return f"Plant '{name}' is healthy!"


def test_plant_checks():
    print("\nTesting normal watering...")
    check_plant_health("tomato", 5, 6)
    print("\nTesting empty plant name...")
    check_plant_health("", 5, 6)
    print("\nTesting bad water level...")
    check_plant_health("tomato", 15, 6)
    print("\nTesting bad sunlight hours...")
    check_plant_health("tomato", 5, 0)
    print("All error raising tests completed!")


def main():
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()


if __name__ == "__main__":
    main()
