def water_plants(plant_list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None")
            print("Watering", plant)
    except ValueError as e:
        print("Error:", e, "- invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    err_plants = ["tomato", None, "carrots"]
    plants = ["tomato", "lettuce", "carrots"]
    print("Testing normal watering...")
    water_plants(plants)
    print("Watering completed successfully!\n")
    print("\nTesting with error...")
    water_plants(err_plants)
    print("\nCleanup always happens, even with errors!")


def main():
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()
