class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloomed: bool):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = bloomed

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        if not self.bloomed:
            self.bloomed = True

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm {self.age} days old\n"
              f" color: {self.color}")
        if not self.bloomed:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")

    def do_thing(self) -> None:
        self.show()
        self.bloom()
        self.show()


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of",
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days old\n",
              f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")

    def do_thing(self) -> None:
        self.show()
        self.produce_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, nutri_value: int):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutri_value = nutri_value

    def grow(self) -> None:
        self.height = round(self.height + 2.1, 1)

    def age_up(self) -> None:
        self.age += 1

    def nutri_up(self) -> None:
        self.nutri_value += 1

    def simulate_week(self) -> None:
        self.show()
        print(f"[make {self.name} grow and age for 20 days]")
        for day in range(1, 21):
            self.grow()
            self.age_up()
            self.nutri_up()
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old\n",
              f" Harvest season: {self.harvest_season}\n",
              f" Nutritional value: {self.nutri_value}")

    def do_thing(self) -> None:
        self.simulate_week()


def main():
    print("=== Garden Plant Types ===")
    flowers = [("Rose", 15.0, 10, "red", False)]
    tree = [("Oak", 200.0, 365, 5.0)]
    vegetable = [("Tomato", 5.0, 10, "April", 0)]
    print("=== Flower")
    for name, height, age, color, bloomed in flowers:
        Flower(name, height, age, color, bloomed).do_thing()
    print()
    print("=== Tree")
    for name, height, age, trunk_diameter, in tree:
        Tree(name, height, age, trunk_diameter).do_thing()
    print()
    print("=== Vegetable")
    for name, height, age, harvest_season, nutri_value in vegetable:
        Vegetable(name, height, age, harvest_season, nutri_value).do_thing()
    print()


if __name__ == "__main__":
    main()
