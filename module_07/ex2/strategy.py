from abc import ABC, abstractmethod


class InvalidStrategyException(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature) -> list[str]:
        pass
