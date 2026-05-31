from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined() -> str:
        return ", ".join([spell1(), spell2()])
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified() -> int:
        return base_spell() * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster() -> str:
        if condition(spell()):
            return spell()
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence():
        return [spell() for spell in spells]
    return sequence


def main() -> None:
    print('\nTesting spell combiner...')

    def fireball() -> str:
        return "Fireball hits Dragon"

    def heal() -> str:
        return "Heals Dragon"
    combined = spell_combiner(fireball, heal)
    print("Combined spell result:", combined())
    print()

    def power_ten() -> int:
        return 10
    amp_power = power_amplifier(power_ten, 3)
    print('Testing power amplifier...')
    print(f"Original: {power_ten()}, "
          f"Amplified: {amp_power()}\n")

    # def check_spell(spell: str) -> bool:
    #     return spell == fireball()
    # verif_spell = conditional_caster(check_spell, heal)
    # print('Testing conditional caster...')
    # print(verif_spell(), "\n")

    # lst_spells = spell_sequence([heal, fireball])
    # print('Testing spell sequence...')
    # print(lst_spells())


if __name__ == "__main__":
    main()
