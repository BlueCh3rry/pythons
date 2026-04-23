from ex0.creaturefactory import FlameFactory, AquaFactory
from ex1.creaturefactory import HealingCreatureFactory
from ex1.creaturefactory import TransformCreatureFactory
from ex2.strategies import NormalStrategy, AggressiveStrategy
from ex2.strategies import DefensiveStrategy
from ex2.strategy import InvalidStrategyException


def fight(creature_a, strategy_a, creature_b, strategy_b) -> bool:
    print("* Battle *")
    print(creature_a.describe())
    print(" vs.")
    print(creature_b.describe())
    print(" now fight!")

    try:
        for action in strategy_a.act(creature_a):
            print(action)
        for action in strategy_b.act(creature_b):
            print(action)
    except InvalidStrategyException as e:
        print(f"Battle error, aborting tournament: {e}")
        return False
    return True


def run_tournament(opponents) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            creature_a, strategy_a = opponents[i]
            creature_b, strategy_b = opponents[j]
            combat = fight(creature_a, strategy_a, creature_b, strategy_b)
            if not combat:
                return


def main() -> None:
    print("Tournament 0 (basic)")
    healing_factory = HealingCreatureFactory()
    opponents0 = [
        (healing_factory.create_base(), NormalStrategy()),
        (healing_factory.create_evolved(), DefensiveStrategy())]
    run_tournament(opponents0)

    print("\nTournament 1 (error)")
    flame_factory = FlameFactory()
    opponents1 = [
        (flame_factory.create_base(), AggressiveStrategy()),
        (healing_factory.create_base(), DefensiveStrategy())]
    run_tournament(opponents1)

    print("\nTournament 2 (multiple)")
    aqua_factory = AquaFactory()
    transform_factory = TransformCreatureFactory()
    opponents2 = [
        (aqua_factory.create_base(), NormalStrategy()),
        (healing_factory.create_base(), DefensiveStrategy()),
        (transform_factory.create_base(), AggressiveStrategy())]
    run_tournament(opponents2)


if __name__ == "__main__":
    main()
