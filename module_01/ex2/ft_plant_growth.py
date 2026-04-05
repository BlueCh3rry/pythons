class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float):
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def get_info(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self.age} days old"

    def grow(self) -> None:
        self.height += self.growth_rate

    def age_up(self) -> None:
        self.age += 1

    def simulate_week(self) -> None:
        for day in range(1, 8):
            print(f"=== Day {day} ===")
            print(self.get_info())
            self.grow()
            self.age_up()

        print(f"Growth this week: {day-1}cm\n")


def main() -> None:
    p1 = Plant("Rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    p1.simulate_week()


if __name__ == "__main__":
    main()
