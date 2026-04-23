def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    if validate_ingredients(ingredients) == "VALID":
        return (f"Spell recorded: {spell_name}"
                f" ({validate_ingredients(ingredients)})")
    return (f"Spell rejected: {spell_name}"
            f" ({validate_ingredients(ingredients)})")
