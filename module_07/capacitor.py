from ex1.creaturefactory import HealingCreatureFactory
from ex1.creaturefactory import TransformCreatureFactory


def main() -> None:
    print("Testing Creature with healing capability")
    fact = HealingCreatureFactory()
    print(" base:")
    p1 = fact.create_base()
    print(p1.describe())
    print(p1.attack())
    print(p1.heal())
    print(" evolved:")
    p2 = fact.create_evolved()
    print(p2.describe())
    print(p2.attack())
    print(p2.heal())

    print("\nTesting Creature with transform capability")
    fact2 = TransformCreatureFactory()
    print(" base:")
    p3 = fact2.create_base()
    print(p3.describe())
    print(p3.attack())
    print(p3.revert())
    print(" evolved:")
    p4 = fact2.create_evolved()
    print(p4.describe())
    print(p4.attack())
    print(p4.revert())


if __name__ == "__main__":
    main()
