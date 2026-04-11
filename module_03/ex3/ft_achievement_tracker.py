import random


def achievements_pool() -> list:
    return [
        "first_kikoha", "its_over_9000", "silver_sword",
        "namek_explorer", "kamehameha",
        "yamcha_down", "dragon_ball",
        "frieza_slayer", "earth_savior", "shenron",
        "super_saiyan"
    ]


def gen_player_achievements() -> set:
    pool = achievements_pool()
    nb = random.randint(1, len(pool))
    return set(random.sample(pool, nb))


def players_init() -> dict:
    return {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }


def shared_badge_all(players: dict) -> set:
    badge_sets = list(players.values())
    if not badge_sets:
        return set()
    return set.intersection(*badge_sets)


def all_unique_badges(players: dict) -> set:
    return set.union(*players.values())


def unique_badges_per_player(players: dict) -> dict:
    result = {}

    for name, badges in players.items():
        others: set = set()
        for other_name, other_badges in players.items():
            if other_name != name:
                others = others.union(other_badges)
        unique = badges.difference(others)
        result[name] = unique
    return result


def missing_badges_per_player(players: dict) -> dict:
    all_badges = all_unique_badges(players)
    result = {}
    for name, badges in players.items():
        result[name] = set.difference(all_badges, badges)
    return result


def main():
    print("=== Achievement Tracker System ===\n")

    players = players_init()
    for name, badges in players.items():
        print(f"Player {name} achievements: {badges}")

    all_badges = all_unique_badges(players)
    print(f"\nAll distinct achievements: {all_badges}")

    common = shared_badge_all(players)
    print(f"\nCommon achievement: {common}\n")

    unique = unique_badges_per_player(players)
    for name, badges in unique.items():
        print(f"Only {name} has: {badges}")
    print()

    missing = missing_badges_per_player(players)
    for name, badges in missing.items():
        print(f"{name} is missing: {badges}")


if __name__ == "__main__":
    main()
