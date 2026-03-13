class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        return f"Created: {self.name} ({self.height}cm {self.age} days)"


def create_plant(name, height, age):
    return Plant(name, height, age)


def main():
    print("=== Plant Factory Output ===\n")
    plants = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]
    count = 0
    for name, height, age in plants:
        count += 1
        print(create_plant(name, height, age).get_info())
    print("\nTotal plants created:", count)


if __name__ == "__main__":
    main()