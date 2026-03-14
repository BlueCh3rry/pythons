class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def growth(self):
        count = 1
        print("=== Day", count, "===")
        print(self.get_info())
        for count in range(1, 7):
            self.height += 1
            self.age += 1
        print("=== Day", count, "===")
        print(self.get_info())
        print(f"Growth this week: +{count}cm")
        print()


def main():
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    print(p1.growth())
    print(p2.growth())


if __name__ == "__main__":
    main()
