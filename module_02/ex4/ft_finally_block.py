class PlantError(Exception):
    """Error related to plant problems"""
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plants(plant_name: str) -> None:
    try:
        if plant_name.capitalize():
            print(f"Watering {plant_name} [OK]")
    except PlantError:
        raise PlantError(f"Invalid plant name to water: {plant_name}")


def test_watering_system() -> None:
    plants = ["Tomato", "Lettuce", "Carrots"]
    err_plants = ["Tomato", "lettuce", "Carrots"]
    print("Testing normal watering...")
    print("Opening watering system")
    try:
        for plant in plants:
            water_plants(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        for plant2 in err_plants:
            water_plants(plant2)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()
