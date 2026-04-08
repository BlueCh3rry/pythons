class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    @classmethod
    def anonymous(self):
        pass

    @staticmethod
    def age_check(age) -> bool:
        return age > 365


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloomed: bool):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = bloomed

    class Stats(Plant):
        def __init__(self):
            super().__init__(self)
            self.stats_height = 0
            self.stats_age = 0

        def grow(self, val: float) -> None:
            self.height = round(self.height + val, 1)
            self.stats_height += 1

        def age_up(self, val: int) -> None:
            self.age += val

        def get_grow(self) -> float:
            return self.stats_height

        def get_age(self) -> int:
            return self.age

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.Stats.grow(8.0)
        if not self.bloomed:
            self.bloomed = True

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm {self.age} days old\n"
              f" color: {self.color}")
        if not self.bloomed:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")
        display_stats(self)

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
        display_stats(self)

    def do_thing(self) -> None:
        self.show()
        self.produce_shade()


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloomed: bool, seeds: int):
        super().__init__(name, height, age, color, bloomed)
        self.seed = seeds

    def seed_up(self, val: int) -> None:
        self.seed += val

    def simulate(self) -> None:
        self.show()
        print(f"[make {self.name} grow, age and bloom]")
        self.Stats.grow(8.0)
        self.Stats.age_up(20)
        self.seed_up(42)
        self.show()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old\n",
              f" color: {self.color}")
        if not self.bloomed:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")
        print(f" Seeds: {self.seed}")
        # display_stats()

    def do_thing(self) -> None:
        self.simulate()


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    print(f"Stats: {plant.Stats.get_grow()} grow, {plant.Stats.get_age()} age, {plant.Stats.get_age()} show")


def main():
    print("=== Garden statistics ===")
    flowers = [("Rose", 15.0, 10, "red", False)]
    tree = [("Oak", 200.0, 365, 5.0)]
    seed = [("Tomato", 5.0, 10, "yellow", False, 0)]
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.age_check(30)}")
    print(f"Is 400 days more than a year? -> {Plant.age_check(400)}\n")
    print("=== Flower")
    for name, height, age, color, bloomed in flowers:
        Flower(name, height, age, color, bloomed).do_thing()
    print()
    print("=== Tree")
    for name, height, age, trunk_diameter, in tree:
        Tree(name, height, age, trunk_diameter).do_thing()
    print()
    print("=== Seed")
    for name, height, age, color, bloomed, seeds in seed:
        Seed(name, height, age, color, bloomed, seeds).do_thing()
    print()


if __name__ == "__main__":
    main()

"""
=== Flower


[asking the rose to grow and bloom]
Rose: 23.0cm, 10 days old
Color: red
Rose is blooming beautifully!
[statistics for Rose]
Stats: 1 grow, 0 age, 2 show

=== Tree

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
