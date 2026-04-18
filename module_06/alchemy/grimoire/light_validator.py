from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ing = light_spell_allowed_ingredients()
    if ingredients in ing:
        return "VALID"
    else:
        return "INVALID"
