from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ing = dark_spell_allowed_ingredients()
    if ingredients in ing:
        return "VALID"
    else:
        return "INVALID"
