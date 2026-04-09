class PlantError(Exception):
    """Error related to plant problems"""
    "Plant error"


def water_plants(plant_name: str) -> None:
    print("Opening watering system")
    if plant_name in ("cactus, succulents, lavender, rosemary, lettuce"):
        raise PlantError(f"Invalid plant name to water: {plant_name}")
    try:
        print(f"Watering {plant_name} [OK]")
    except PlantError:
        raise PlantError


def test_watering_system() -> str:
    plants = ["tomato", "lettuce", "carrots"]
    err_plants = ["tomato", "cactus", "lettuce"]
    print("Testing normal watering...")
    for plant in plants:
        try:
            water_plants(plant)
        except PlantError as e:
            return f"Caught PlantError: {e}"
        finally:
            print("Closing watering system")

    print("Testing invalid plants...")
    for plant2 in err_plants:
        try:
            water_plants(plant2)
        except PlantError as e:
            print(f"Caught PlantError: {e}")
            return ".. ending tests and returning to main"
        finally:
            print("Closing watering system")
    return "\nCleanup always happens, even with errors!"


def main() -> None:
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()
