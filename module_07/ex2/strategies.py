from .strategy import BattleStrategy, InvalidStrategyException
from typing import Any


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return True

    def act(self, creature: Any):
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return hasattr(creature, "transform")

    def act(self, creature: Any) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy")
        return [
            creature.transform(),
            creature.attack(),
            creature.revert()]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Any) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature: Any) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}'"
                " for this defensive strategy")
        return [
            creature.attack(),
            creature.heal()]
