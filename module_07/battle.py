from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_creature(fact: CreatureFactory) -> None:
    print("Testing factory")
    p1 = fact.create_base()
    print(p1.describe())
    print(p1.attack())
    p2 = fact.create_evolved()
    print(p2.describe())
    print(p2.attack())


def battle(fact1: CreatureFactory, fact2: CreatureFactory) -> None:
    print("Testing battle")
    p1 = fact1.create_base()
    p3 = fact2.create_base()
    print(p1.describe())
    print(" vs.")
    print(p3.describe())
    print(" fight!")
    print(p1.attack())
    print(p3.attack())


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    test_creature(flame_factory)
    print()
    test_creature(aqua_factory)
    print()
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()
