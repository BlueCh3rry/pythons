from .elements import create_fire, create_water

__version__ = "1.0.0"
__author__ = "Master Pythonicus"


def main() -> None:
    print(f"alchemy.create_fire(): {create_fire()}:")
    print(f"alchemy.create_water(): {create_water()}")


if __name__ == "__main__":
    main()
