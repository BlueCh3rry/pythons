from ex0.creaturefactory import FlameFactory, AquaFactory, CreatureFactory
from ex1.creaturefactory import HealingCreatureFactory
from ex1.creaturefactory import TransformCreatureFactory
from ex2.strategies import NormalStrategy, AggressiveStrategy
from ex2.strategies import DefensiveStrategy
from ex2.strategy import InvalidStrategyException, BattleStrategy
from typing import List, Tuple


Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(pair: Tuple[Opponent, Opponent]) -> bool:
    factory_a, strategy_a = pair[0]
    factory_b, strategy_b = pair[1]
    creature_a = factory_a.create_base()
    creature_b = factory_b.create_base()
    print("\n* Battle *")
    print(creature_a.describe())
    print("vs.")
    print(creature_b.describe())
    print("now fight!")

    try:
        for action in strategy_a.act(creature_a):
            print(action)
        for action in strategy_b.act(creature_b):
            print(action)
    except InvalidStrategyException as e:
        print(f"Battle error, aborting tournament: {e}")
        return False
    return True


def run_tournament(opponents: List[Opponent]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            if not battle((opponents[i], opponents[j])):
                return


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents0: List[Opponent] = [
        (flame_factory, NormalStrategy()),
        (healing_factory, DefensiveStrategy()),
    ]
    run_tournament(opponents0)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents1: List[Opponent] = [
        (flame_factory, AggressiveStrategy()),
        (healing_factory, DefensiveStrategy()),
    ]
    run_tournament(opponents1)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents2: List[Opponent] = [
        (aqua_factory, NormalStrategy()),
        (healing_factory, DefensiveStrategy()),
        (transform_factory, AggressiveStrategy()),
    ]
    run_tournament(opponents2)


if __name__ == "__main__":
    main()
