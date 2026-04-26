from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, elem: str):
        self.name = name
        self.elem = elem

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.elem} type Creature"


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self):
        return f"{self.name} attacks with Ember!"


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire")

    def attack(self):
        return f"{self.name} attacks with Flamethrower!"


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self):
        return f"{self.name} attacks with Water Gun!"


class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water")

    def attack(self):
        return f"{self.name} attacks with Hydro Pump!"
