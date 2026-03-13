class SecurePlant:
    def __init__(self, name):
        self.name = name
        self.__height = 0
        self.__age = 0

    def set_height(self, height):
        if (height < 0):
            print("Invalid operation attempted: height", height, "cm [REJECTED]\nSecurity: Negative height rejected")
            return 0
        else:
            self.__height = height
            print("Height updated:", height, "cm [OK]")
            return 1

    def set_age(self, age):
        if (age < 0):
            print("Invalid operation attempted: days", age, "days [REJECTED]\nSecurity: Negative days rejected")
            return 0
        else:
            self.__age = age
            print("Age updated:", age, "days [OK]")
            return 

    def current_info(self):
        return f"Current plant: {self.name} ({self.height}cm, {self.age} days)"


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
