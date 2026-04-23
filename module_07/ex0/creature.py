from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, elem: str, atk: str):
        self.name = name
        self.elem = elem
        self.atk = atk

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.elem} type Creature"


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire", "Ember")

    def attack(self):
        return f"{self.name} attacks with {self.atk}!"


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire", "Flamethrower")

    def attack(self):
        return f"{self.name} attacks with {self.atk}!"


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water", "Water Gun")

    def attack(self):
        return f"{self.name} attacks with {self.atk}!"


class Torragon(Creature):
    def __init__(self):
        super().__init__("Torragon", "Water", "Hydro Pump")

    def attack(self):
        return f"{self.name} attacks with {self.atk}!"
