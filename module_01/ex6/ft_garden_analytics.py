class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.stats = Plant.Stats()

    class Stats():
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0
            self.shade_count = 0

        def grow(self) -> None:
            self.grow_count += 1

        def age_up(self) -> None:
            self.age_count += 1

        def show(self) -> None:
            self.show_count += 1

        def produce_shade(self) -> None:
            self.shade_count += 1

    @classmethod
    def anonymous(self):
        return self("Unknown plant", 0.0, 0)

    @staticmethod
    def age_check(age) -> bool:
        return age > 365

    def grow(self, val: float) -> None:
        self.height = round(self.height + val, 1)
        self.stats.grow()

    def age_up(self, val: int) -> None:
        self.age += val
        self.stats.age_up()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        if isinstance(self, (Flower, Seed)):
            print(f" color: {self.color}")
            if not self.bloomed:
                print(f" {self.name} has not bloomed yet")
            else:
                print(f" {self.name} is blooming beautifully!")
            if isinstance(self, Seed):
                print(f" Seeds: {self.seed}")
        if isinstance(self, Tree):
            print(f"Trunk diameter: {round(self.trunk_diameter, 1)}cm")
        self.stats.show()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloomed: bool):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = bloomed

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self.grow(8.0)
        if not self.bloomed:
            self.bloomed = True

    def do_thing(self) -> None:
        self.show()
        display_stats(self)
        self.bloom()
        self.show()
        display_stats(self)


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = diameter

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of",
              f"{self.height}cm long and {self.trunk_diameter}cm wide.")
        self.stats.produce_shade()

    def do_thing(self) -> None:
        self.show()
        display_stats(self)
        self.produce_shade()
        display_stats(self)


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, bloomed: bool, seeds: int):
        super().__init__(name, height, age, color, bloomed)
        self.seed = seeds

    def seed_up(self, val: int) -> None:
        self.seed += val

    def simulate(self) -> None:
        self.show()
        display_stats(self)
        print(f"[make {self.name} grow, age and bloom]")
        self.grow(8.0)
        self.age_up(20)
        self.seed_up(42)
        self.show()
        display_stats(self)

    def do_thing(self) -> None:
        self.simulate()


def display_stats(self: Plant | Flower | Tree | Seed) -> None:
    print(f"[statistics for {self.name}]")
    print(f"Stats: {self.stats.grow_count} grow, {self.stats.age_count} age,",
          f"{self.stats.show_count} show")
    if isinstance(self, Tree):
        print(f" {self.stats.shade_count} shade")


def main():
    print("=== Garden statistics ===")
    flowers = [("Rose", 15.0, 10, "red", False)]
    tree = [("Oak", 200.0, 365, 5.0)]
    seed = [("Sunflower", 5.0, 10, "yellow", False, 0)]
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

    print("== Anonymous")
    secret_plant = Plant.anonymous()
    secret_plant.show()
    display_stats(secret_plant)


if __name__ == "__main__":
    main()
