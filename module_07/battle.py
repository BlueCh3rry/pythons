from ex0.creaturefactory import FlameFactory, AquaFactory


def main() -> None:
    print("Testing factory")
    fact = FlameFactory()
    p1 = fact.create_base()
    print(p1.describe())
    print(p1.attack())
    p2 = fact.create_evolved()
    print(p2.describe())
    print(p2.attack())

    print("\nTesting factory")
    fact2 = AquaFactory()
    p3 = fact2.create_base()
    print(p3.describe())
    print(p3.attack())
    p4 = fact2.create_evolved()
    print(p4.describe())
    print(p4.attack())

    print("\nTesting battle")
    print(p1.describe())
    print(" vs.")
    print(p3.describe())
    print(" fight!")
    print(p1.attack())
    print(p3.attack())


if __name__ == "__main__":
    main()
