# ex5 FAIT et non verifier
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(self.name, " (Flower): ", self.height, "cm, ", self.age, " days, summer harvest", sep="")
        print(self.name, "is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(self.name, " (Tree): ", self.height, "cm, ", self.age, " days, ", self.trunk_diameter, "diameter", sep="")
        print(self.name, "provides", self.trunk_diameter, "square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutri_value):
        super().__init__(name, height, age)
        if harvest_season not in ("winter", "spring", "summer", "autumn"):
            print(harvest_season, "Invalid season entered")
            # return 0
        self.harvest_season = harvest_season
        self.nutri_value = nutri_value

    def get_info(self):
        print(self.name, " (Vegetable): ", self.height, "cm, ", self.age, " days, ", self.harvest_season, "harvest", sep="")
        print(self.name, "is rich in vitamin C\n")


def main():
    print("=== Garden Plant Types ===\n")
    flowers = [("Rose", 25, 30, "red")]
    tree = [("Oak", 500, 1825, 50)]
    vegetable = [("Tomato", 25, 30, "summer", 5)]
    for name, height, age, color in flowers:
        Flower(name, height, age, color).bloom()

    for name, height, age, trunk_diameter, in tree:
        Tree(name, height, age, trunk_diameter).produce_shade()

    for name, height, age, harvest_season, nutri_value in vegetable:
        Vegetable(name, height, age, harvest_season, nutri_value).get_info()


if __name__ == "__main__":
    main()
