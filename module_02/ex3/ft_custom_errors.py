class GardenError(Exception):
    """Base class for all garden-related errors"""
    def __init__(self, message="General garden error"):
        super().__init__(message)


class PlantError(GardenError):
    """Error related to plant problems"""
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    """Error related to watering problems"""
    def __init__(self, message="Unknown watering error"):
        super().__init__(message)


def garden_operations(action: str) -> None:
    if action == "plant":
        raise PlantError("The tomato plant is wilting!")
    elif action == "water":
        raise WaterError("Not enough water in the tank!")
    else:
        raise GardenError("Unknown garden operation!")


def custom_error_types() -> None:
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

    print("\nTesting catching all garden errors...")
    try:
        garden_operations("plant")
    except GardenError as e:
        print("Caught GardenError:", e)

    try:
        garden_operations("water")
    except GardenError as e:
        print("Caught GardenError:", e)
    print("\nAll custom error types work correctly!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    custom_error_types()


if __name__ == "__main__":
    main()
