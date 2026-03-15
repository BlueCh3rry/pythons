class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def growth(self) -> None:
        count = 1
        print("=== Day", count, "===")
        print(self.get_info())
        for count in range(1, 7):
            self.height += 1
            self.age += 1
        print("=== Day", count + 1, "===")
        print(self.get_info())
        print(f"Growth this week: +{count}cm")
        print()


def main() -> None:
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p1.growth()
    p2.growth()


if __name__ == "__main__":
    main()
