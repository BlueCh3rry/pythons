from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ing = dark_spell_allowed_ingredients()
    words = [w.strip().lower() for w in ingredients.split(',')]
    for word in words:
        if word in ing:
            return "VALID"
    return "INVALID"
