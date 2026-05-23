#!/usr/bin/python3


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    return (spell1(), spell2(),)


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    return base_spell() * multiplier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def return_fizzled(value) -> str:
        return "Spell fizzled"

    damage = 5
    if condition(damage):
        return spell
    else:
        return return_fizzled


def spell_sequence(spells: list[callable]) -> callable:
    arg = 5
    results = []
    for spell in spells:
        results.append(spell(arg))
    return results


def main() -> None:
    print('=== Testing spell combiner... ===')

    def fireball() -> str:
        return "Fireball hits Dragon"

    def heal() -> str:
        return "Heals Dragon"

    a, b = spell_combiner(fireball, heal)
    print(f"Combined spell result: {a}, {b}")
    print('')

    def deal_ten_damage() -> int:
        return 10

    print('=== Testing power amplifier... ===')
    print(f"Original: {deal_ten_damage()}, "
          f"Amplified: {power_amplifier(deal_ten_damage, 3)}")
    print('')

    print('=== Testing conditional caster... ===')

    def condition(damage: int) -> bool:
        if damage > 10:
            return False
        return True

    def lightning(damage) -> str:
        return f"Stroke with {damage} damages."

    print(f"Result: {conditional_caster(condition, lightning)(5)}")
    print('')

    print('=== Testing conditional caster... ===')
    print(f"Result: {spell_sequence([lightning, lightning, lightning])}")
    print('')

    return None


if __name__ == "__main__":
    main()
