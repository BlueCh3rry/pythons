def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda arti: arti["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": sum(list(map(lambda m: m["power"], mages))) / len(mages),
    }


def main() -> None:
    artifacts = [
        {"name": "Fire Staff", "power": 92},
        {"name": "Crystal Orb", "power": 85},
    ]

    spells = ["fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    item = artifact_sorter(artifacts)
    print(f"{item[0]['name']} ({item[0]['power']} power) comes before",
          f"{item[1]['name']} ({item[1]['power']} power)\n")

    # print("Testing power filter (min: 90)...")
    # for item1 in power_filter(artifacts, 90):
    #     print(f"{item1['name']} - {item1['power']}")
    # print()

    print("Testing spell transformer...")
    for item2 in spell_transformer(spells):
        print(f"{item2} ", end="")
    print("\n")

    # print("Testing spell stats...")
    # stats = mage_stats(artifacts)
    # print(
    #     f"Max power: {stats['max_power']}\n"
    #     f"Min power: {stats['min_power']}\n"
    #     f"Average power: {stats['avg_power']}"
    # )
    # print()


if __name__ == "__main__":
    main()
