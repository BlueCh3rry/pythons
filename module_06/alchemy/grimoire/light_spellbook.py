from .light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    if validate_ingredients(ingredients):
        return "Spell recorded"
    else:
        return "Spell rejected"
