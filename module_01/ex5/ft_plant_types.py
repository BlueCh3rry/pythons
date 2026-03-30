class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name}: {self.height}cm,"
              f"{self.age} days, "
              f"color:")
        print(self.name, "is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def produce_shade(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days,",
              f"Trunk Diameter: {round(self.trunk_diameter, 1)}cm")
        print(f"{self.name} provides",
              f"{self.trunk_diameter} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutri_value):
        super().__init__(name, height, age)
        if harvest_season not in ("winter", "spring", "summer", "autumn"):
            print(harvest_season, "Invalid season entered")
        self.harvest_season = harvest_season
        self.nutri_value = nutri_value

    def grow(self) -> None:
        self.height += 

    def age_up(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days,",
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutri_value}\n")


def main():
    print("=== Garden Plant Types ===")
    flowers = [("Rose", 25, 30, "red")]
    tree = [("Oak", 500, 1825, 75)]
    vegetable = [("Tomato", 25, 30, "summer", 30)]
    print("=== Flower")
    for name, height, age, color in flowers:
        Flower(name, height, age, color).bloom()

    print("=== Tree")
    for name, height, age, trunk_diameter, in tree:
        Tree(name, height, age, trunk_diameter).produce_shade()

    print("=== Vegetable")
    for name, height, age, harvest_season, nutri_value in vegetable:
        Vegetable(name, height, age, harvest_season, nutri_value).get_info()


if __name__ == "__main__":
    main()
