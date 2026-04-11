class PlantError(Exception):
    """Error related to plant problems"""
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    plants = ["Tomato", "Lettuce", "Carrots"]
    err_plants = ["Tomato", "lettuce", "Carrots"]
    print("Testing normal watering...")
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Opening watering system")
    try:
        for plant2 in err_plants:
            water_plant(plant2)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")
        print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()
