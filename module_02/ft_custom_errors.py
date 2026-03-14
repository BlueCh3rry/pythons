class GardenError(Exception):
    """Base class for all garden-related errors"""
    pass


class PlantError(GardenError):
    """Error related to plant problems"""
    pass


class WaterError(GardenError):
    """Error related to watering problems"""
    pass


def garden_operations(action: str) -> None:
    if action == "plant":
        raise PlantError("The tomato plant is wilting!")
    elif action == "water":
        raise WaterError("Not enough water in the tank!")
    else:
        raise GardenError("Unknown garden operation!")


def custom_error_types() -> str:
    try:
        print("Testing PlantError...")
        garden_operations("plant")
    except PlantError as e:
        print("Caught PlantError:", e)
    try:
        print("\nTesting WaterError...")
        garden_operations("water")
    except WaterError as e:
        print("Caught WaterError:", e)
    try:
        garden_operations("plant")
        garden_operations("water")
    except PlantError as e:
        print("Caught PlantError:", e)
    except WaterError as e:
        print("Caught WaterError:", e)
    return "\nAll custom error types work correctly!"


def main() -> None:
    print("=== Custom Garden Error Demo ===\n")
    print(custom_error_types())


if __name__ == "__main__":
    main()
