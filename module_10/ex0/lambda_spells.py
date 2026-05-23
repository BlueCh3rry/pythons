#!/usr/bin/python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


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
        {"name": "Lightning Rod", "power": 79, "type": "weapon"},
        {"name": "Ice Wand", "power": 93, "type": "armor"},
        {"name": "Storm Crown", "power": 112, "type": "focus"},
        {"name": "Light Prism", "power": 60, "type": "accessory"},
    ]
    mages = [
        {"name": "Ember", "power": 61, "element": "lightning"},
        {"name": "Nova", "power": 83, "element": "ice"},
        {"name": "Luna", "power": 92, "element": "ice"},
        {"name": "Nova", "power": 98, "element": "fire"},
        {"name": "Luna", "power": 69, "element": "earth"},
    ]
    spells = ["lightning", "tsunami", "heal", "darkness"]

    print("=== Testing artifact sorter... ===")
    for item in artifact_sorter(artifacts):
        print(f"{item['name']} - {item['power']}")
    print("")

    print("=== Testing power filter (min: 90)... ===")
    for item in power_filter(artifacts, 90):
        print(f"{item['name']} - {item['power']}")
    print("")

    print("=== Testing spell transformer... ===")
    for item in spell_transformer(spells):
        print(item)
    print("")

    print("=== Testing mages stats... ===")
    stats = mage_stats(mages)
    print(
        f"Max power: {stats['max_power']}\n"
        f"Min power: {stats['min_power']}\n"
        f"Average power: {stats['avg_power']}"
    )
    print("")
    return None


if __name__ == "__main__":
    main()
