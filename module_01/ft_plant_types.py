class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm,",
              f"{self.age} days, red color")
        print(self.name, "is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days,",
              f"{self.trunk_diameter}cm diameter")
        print(f"{self.name} provides",
              f"{self.trunk_diameter} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutri_value):
        super().__init__(name, height, age)
        if harvest_season not in ("winter", "spring", "summer", "autumn"):
            print(harvest_season, "Invalid season entered")
        self.harvest_season = harvest_season
        self.nutri_value = nutri_value

    def get_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days,",
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in vitamin {self.nutri_value}\n")


def main():
    print("=== Garden Plant Types ===\n")
    flowers = [("Rose", 25, 30, "red")]
    tree = [("Oak", 500, 1825, 75)]
    vegetable = [("Tomato", 25, 30, "summer", 'C')]
    for name, height, age, color in flowers:
        Flower(name, height, age, color).bloom()

    for name, height, age, trunk_diameter, in tree:
        Tree(name, height, age, trunk_diameter).produce_shade()

    for name, height, age, harvest_season, nutri_value in vegetable:
        Vegetable(name, height, age, harvest_season, nutri_value).get_info()


if __name__ == "__main__":
    main()
