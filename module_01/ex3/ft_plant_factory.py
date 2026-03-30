class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return (f"Created: {self.name} "
                f"{round(self.height, 1)}cm, {self.age} days old")


def create_plant(name: str, height: float, age: int) -> Plant:
    return Plant(name, height, age)


def main() -> None:
    print("=== Plant Factory Output ===")
    plants = [
        ("Rose", 25.0, 30),
        ("Oak", 200.0, 365),
        ("Cactus", 5.0, 90),
        ("Sunflower", 80.0, 45),
        ("Fern", 15.0, 120),
    ]
    for name, height, age in plants:
        print(create_plant(name, height, age).get_info())


if __name__ == "__main__":
    main()
