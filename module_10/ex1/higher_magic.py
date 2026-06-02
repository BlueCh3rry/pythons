from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def main() -> None:
    print('\nTesting spell combiner...')

    def fireball(target: str, power: int) -> str:
        if power <= 0:
            return f"Fireball hits {target}"
        return f"Fireball hits {power} DMG to {target}"

    def heal(target: str, power: int) -> str:
        if power <= 0:
            return f"Heals {target}"
        return f"Heals {target} {power} HP"
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", combined("Dragon", 0))
    print()

    def blast(target: str, power: int) -> str:
        if power <= 0:
            return f"Blast {target}"
        return f"Blasting {target}, {power} DMG"
    amp_blast = power_amplifier(blast, 3)
    print('Testing power amplifier...')
    print(
        f"Original: {blast('Wyvern', 10)}\n"
        f"Amplified: {amp_blast('Wyvern', 10)}\n"
    )

    # def condition(target: str, power: int) -> bool:
    #     if target and power:
    #         return power >= 10
    #     return False
    # verif_spell = conditional_caster(condition, fireball)
    # print('Testing conditional caster...')
    # print("Badly done: ", verif_spell("Snake", 0))
    # print("Well done: ", verif_spell("Snake", 50), "\n")
    
    # lst_spells = spell_sequence([heal, fireball])
    # print('Testing spell sequence...')
    # print(lst_spells("Turtle", 48), "\n")


if __name__ == "__main__":
    main()
