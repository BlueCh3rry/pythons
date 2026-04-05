class SecurePlant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self._height: float = 0
        self._age: int = 0

    def set_height(self, height: float) -> str:
        if (height < 0):
            print(f"{self._name}: Error, height can't be negative")
            return "Height update rejected"
        else:
            self._height = height
            return f"Height updated: {round(self._height)}cm"

    def set_age(self, age: int) -> str:
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
            return "Age update rejected"
        else:
            self._age = age
            return f"Age updated: {age} days"

    def get_height(self) -> str:
        if self._height > 0:
            return f"{round(self._height, 1)}cm"
        else:
            return "Height not set"

    def get_age(self) -> str:
        if self._age > 0:
            return f"{self._age} days"
        else:
            return "Age not set"

    def info_age_height(self) -> str:
        return f"{self.get_height()}, {self.get_age()}"

    def current_info(self) -> str:
        return f"Current state: {self._name} {self.info_age_height()}"


def create_plant(name, height, age) -> SecurePlant:
    plant = SecurePlant(name, height, age)
    print(f"Plant created: {name}: {height}cm, {age} days old")
    return plant


def main():
    print("=== Garden Security System ===")
    rose = create_plant("Rose", 15.0, 10)
    print()
    print(rose.set_height(25.0))
    print(rose.set_age(30))
    print()
    print(rose.set_height(-5))
    print(rose.set_age(-1))
    print()
    print(rose.current_info())


if __name__ == "__main__":
    main()
