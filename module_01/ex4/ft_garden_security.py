class SecurePlant:
    def __init__(self, name: str):
        self._name = name
        self._height: float = 0
        self._age: int = 0

    def set_height(self, height: float) -> str:
        if (height < 0):
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            return "Security: Negative height rejected"
        else:
            self._height = height
            return f"Height updated: {height}cm [OK]"

    def set_age(self, age: int) -> str:
        if (age < 0):
            print(f"Invalid operation attempted: days {age} days [REJECTED]")
            return "Security: Negative days rejected"
        else:
            self._age = age
            return f"Age updated: {age} days [OK]"

    def get_height(self) -> str:
        if self._height > 0:
            return f"{round(self._height), 1}cm"
        else:
            return "Height not set"

    def get_age(self) -> str:
        if self._age > 0:
            return f"{self._age} days"
        else:
            return "Age not set"
    
    def info_age_height(self) -> str:
        return f"({self.get_height()}, {self.get_age()})"

    def current_info(self) -> str:
        return f"Plant info: {self._name} {self.info_age_height()}"


def create_plant(name, height, age) -> SecurePlant:
    print("Plant created:", name)
    plant = SecurePlant(name)
    print(plant.set_height(height))
    print(plant.set_age(age))
    return plant


def main():
    print("=== Garden Security System ===\n")
    rose = create_plant("Rose", 25, 30)
    print()
    print(rose.set_height(-5))
    print()
    print(rose.current_info())


if __name__ == "__main__":
    main()
