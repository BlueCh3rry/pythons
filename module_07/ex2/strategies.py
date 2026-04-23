from .strategy import BattleStrategy, InvalidStrategyException


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature):
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return hasattr(creature, "transform")

    def act(self, creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}'"
                " for this aggressive strategy")
        return [
            creature.transform(),
            creature.attack(),
            creature.revert()]


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature) -> list[str]:
        if not self.is_valid(creature):
            raise InvalidStrategyException(
                f"Invalid Creature '{creature.name}'"
                " for this defensive strategy"
            )

        return [
            creature.attack(),
            creature.heal()]
