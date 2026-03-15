class PlantError(Exception):
    """Error related to plant problems"""
    pass


class WaterError(Exception):
    """Error related to watering problems"""
    pass


class SunlightError(Exception):
    """Error related to sunlight problems"""
    pass


def check_plant_health(name: str, level: int, hours: int) -> None:
    if not name or not name.strip():
        raise PlantError("Plant name cannot be empty!")
    if level < 1:
        raise WaterError(f"Water level {level} is too low (min 1)")
    elif level > 10:
        raise WaterError(f"Water level {level} is too high (max 10)")
    if hours < 2:
        raise SunlightError(f"Sunlight hours {hours} is too low (min 2)")
    elif hours > 12:
        raise SunlightError(f"Sunlight hours {hours} is too high (max 12)")
    print(f"Plant '{name}' is healthy!")


def test_plant_checks() -> None:
    try:
        print("\nTesting normal watering...")
        check_plant_health("tomato", 5, 6)
    except PlantError as e:
        print(e)

    try:
        print("\nTesting empty plant name...")
        check_plant_health("", 5, 6)
    except PlantError as e:
        print(e)

    try:
        print("\nTesting bad water level...")
        check_plant_health("tomato", 15, 6)
    except WaterError as e:
        print(e)

    try:
        print("\nTesting bad sunlight hours...")
        check_plant_health("tomato", 5, 0)
    except SunlightError as e:
        print(e)

    print("\nAll error raising tests completed!")


def main() -> None:
    print("=== Garden Plant Health Checker ===")
    test_plant_checks()


if __name__ == "__main__":
    main()
