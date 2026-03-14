class SecurePlant:
    def __init__(self, name):
        self._name = name
        self._height = 0
        self._age = 0

    def set_height(self, height):
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print()
            print("Security: Negative days rejected")
            return 0
        else:
            self._height = height
            print("Height updated:", height, "cm [OK]")
            return 1

    def set_age(self, age):
        if (age < 0):
            print(f"Invalid operation attempted: days {age} days [REJECTED]")
            print()
            print("Security: Negative days rejected")
            return 0
        else:
            self._age = age
            print("Age updated:", age, "days [OK]")
            return 0

    def current_info(self):
        return f"Plant info: {self._name} ({self._height}cm, {self._age} days)"


def create_plant(name, height, age):
    print("Plant created:", name)
    plant = SecurePlant(name)
    plant.set_height(height)
    plant.set_age(age)
    return plant


def main():
    print("=== Garden Security System ===\n")
    rose = create_plant("Rose", 25, 30)
    print(rose.current_info())


if __name__ == "__main__":
    main()
