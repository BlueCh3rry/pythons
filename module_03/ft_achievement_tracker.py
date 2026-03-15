
def players_init() -> dict:
    players = {
        "alice": ("first_kikoha", "silver_sword", "dragon_ball", "kamehameha"),
        "bob": ("first_kikoha", "silver_sword", "super_saiyan", "shenron"),
        "charlie": ("yamcha_down", "namek_explorer", "first_kikoha", "shenron")
    }
    return players


def achievement_init() -> dict:
    achievements = {
        "Common": ("first_kikoha", "its_over_9000", "silver_sword"),
        "Rare": ("namek_explorer", "kamehameha"),
        "Epic": ("yamcha_down", "dragon_ball"),
        "Legendary": ("frieza_slayer", "earth_savior", "shenron"),
        "Unique": ("super_saiyan",)
        }
    return achievements


def total_badges(array: dict) -> int:
    count = 0
    for parent, badges in array.items():
        count += len(badges)
    return count


def shared_badge_all(players: dict) -> list:
    badge_sets = [set(badges) for badges in players.values()]
    if not badge_sets:
        return []
    common_badges = set.intersection(*badge_sets)
    return list(common_badges)


def shared_badge(player1: dict, player2: dict) -> set:
    return set(player1) & set(player2)


def missing_badge(player: dict, achievements: dict) -> list:
    all_possible_badges = set().union(*achievements.values())
    if not all_possible_badges:
        return []
    missing_badges = all_possible_badges - set(player)
    return list(missing_badges)


def difference_badge(player1: tuple, player2: tuple) -> list:
    diff_badges = set(player1).difference(set(player2))
    return list(diff_badges)


def find_parent(array: dict, badge_name: str) -> str:
    for parent, badges in array.items():
        if badge_name in badges:
            return parent
    return "Not found, misspell ?"


def compare_player(player1: tuple, player2: tuple) -> None:
    res = shared_badge(player1, player2)
    print(f"Alice vs Bob common: {set(res)}")
    res = difference_badge(player1, player2)
    print(f"Alice unique: {set(res)}")
    res = difference_badge(player2, player1)
    print(f"Bob unique: {set(res)}")


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    players = players_init()
    print(f"Player alice achievements:   {set(players['alice'])}")
    print(f"Player bob achievements:     {set(players['bob'])}")
    print(f"Player charlie achievements: {set(players['charlie'])}\n")

    print("=== Achievement Analytics ===\n")

    achievements = achievement_init()
    print("All unique achievements by rarity:")
    print(f"Common: 	{set(achievements['Common'])}")
    print(f"Rare: 		{set(achievements['Rare'])}")
    print(f"Epic: 		{set(achievements['Epic'])}")
    print(f"Legendary: 	{set(achievements['Legendary'])}")
    print(f"Unique: 	{set(achievements['Unique'])}")
    print(f"total unique achievements: {total_badges(achievements)}")

    print()
    res = shared_badge_all(players)
    print(f"Common to all players: {set(res)}")
    print()
    compare_player(players["alice"], players["bob"])
    # print()
    # res = missing_badge(players["charlie"], achievements)
    # print(f"Charlie missing badges = {set(res)}")


if __name__ == "__main__":
    main()
