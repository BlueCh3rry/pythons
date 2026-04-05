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


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.seed = 0

    def grow(self) -> None:
        self.height = round(self.height + 2.1, 1)
    def age_up(self) -> None:
        self.age += 1
    def seed_up(self) -> None:
        self.seed += 1

    def simulate_week(self) -> None:
        self.show()
        print(f"[make {self.name} grow, age and bloom]")
        for day in range(1, 21):
            self.grow()
            self.age_up()
            self.seed_up()
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old\n",
              f" Harvest season: {self.harvest_season}\n",
              f" Nutritional value: {self.nutri_value}")

    def do_thing(self) -> None:
        self.simulate_week()

    def stats(self)
        

def display_stats()

def check(age) -> bool:
    if age > 365:
        return True
    else:
        return False


def main():
    print("=== Garden statistics ===")
    flowers = [("Rose", 15.0, 10, "red", False)]
    tree = [("Oak", 200.0, 365, 5.0)]
    vegetable = [("Tomato", 5.0, 10, "April", 0)]
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {check(30)}")
    print(f"Is 400 days more than a year? -> {check(400)}")
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


"""

=== Flower
Rose: 15.0cm, 10 days old
Color: red
Rose has not bloomed yet
[statistics for Rose]
Stats: 0 grow, 0 age, 1 show
[asking the rose to grow and bloom]
Rose: 23.0cm, 10 days old
Color: red
Rose is blooming beautifully!
[statistics for Rose]
Stats: 1 grow, 0 age, 2 show
=== Tree
Oak: 200.0cm, 365 days old
Trunk diameter: 5.0cm
[statistics for Oak]
Stats: 0 grow, 0 age, 1 show
0 shade
[asking the oak to produce shade]
Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
[statistics for Oak]
Stats: 0 grow, 0 age, 1 show
1 shade
=== Seed
Sunflower: 80.0cm, 45 days old
Color: yellow
Sunflower has not bloomed yet
Seeds: 0
[make sunflower grow, age and bloom]
Sunflower: 110.0cm, 65 days old
Color: yellow
Sunflower is blooming beautifully!
Seeds: 42
[statistics for Sunflower]
Stats: 1 grow, 1 age, 2 show
=== Anonymous
Unknown plant: 0.0cm, 0 days old
[statistics for Unknown plant]
Stats: 0 grow, 0 age, 1 show
"""
