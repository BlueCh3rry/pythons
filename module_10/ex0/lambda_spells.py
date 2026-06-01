def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda arti: arti["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(
            sum(map(lambda m: m["power"], mages)) / len(mages),
            2),
    }


def main() -> None:
    artifacts = [
        {"name": "Staff", "power": 92, "type": "Fire"},
        {"name": "Orb", "power": 85, "type": "Crystal"},
    ]

    # mages = [
    #     {"name": "Ulduf", "power": 9,  "element": "Rock"},
    #     {"name": "Scarlet",  "power": 153, "element": "Dark"},
    # ]

    spells = ["fireball", "heal", "shield"]

    print("\nTesting artifact sorter...")
    item = artifact_sorter(artifacts)
    print(f"{item[0]['type']} {item[0]['name']} ({item[0]['power']} power)",
          "comes before",
          f"{item[1]['type']} {item[1]['name']} ({item[1]['power']} power)\n")

    # print("Testing power filter (min: 90)...")
    # for item1 in power_filter(mages, 90):
    #     print(f"{item1['name']} - {item1['power']}")
    # print()

    print("Testing spell transformer...")
    for item2 in spell_transformer(spells):
        print(f"{item2} ", end="")
    print("\n")

    # print("Testing spell stats...")
    # stats = mage_stats(mages)
    # print(
    #     f"Max power: {stats['max_power']}\n"
    #     f"Min power: {stats['min_power']}\n"
    #     f"Average power: {stats['avg_power']}"
    # )
    # print()


if __name__ == "__main__":
    main()
