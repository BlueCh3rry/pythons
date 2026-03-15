class PlantError(Exception):
    """Error related to plant problems"""
    pass


class WaterError(Exception):
    """Error related to watering problems"""
    pass


class SunlightError(Exception):
    """Error related to watering problems"""
    pass


def check_plant_health(name: str, level: int, hours: int) -> str:
    if not name:
        raise PlantError("Plant name cannot be empty!")
    if level < 1:
        raise WaterError(f"Water level {level} is too low (min 1)")
    elif level > 10:
        raise WaterError(f"Water level {level} is too high (max 10)")
    if hours < 2:
        raise SunlightError(f"Sunlight hours {hours} is too low (min 2)")
    elif hours > 12:
        raise SunlightError(f"Sunlight hours {hours} is too high (max 12)")
    return f"Plant '{name}' is healthy!"

# faire avec try/except
def test_plant_checks() -> None:
    print("\nTesting normal watering...")
    print(check_plant_health("tomato", 5, 6))
    print("\nTesting empty plant name...")
    print(check_plant_health("", 5, 6))
    print("\nTesting bad water level...")
    print(check_plant_health("tomato", 15, 6))
    print("\nTesting bad sunlight hours...")
    print(check_plant_health("tomato", 5, 0))
    print("All error raising tests completed!")


def main() -> None:
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()


if __name__ == "__main__":
    main()
