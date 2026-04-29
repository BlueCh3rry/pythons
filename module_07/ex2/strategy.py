from abc import ABC, abstractmethod
from typing import Any


class InvalidStrategyException(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Any) -> list[str]:
        pass
