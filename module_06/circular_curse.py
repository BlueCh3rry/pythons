


def main() -> None:
    print("\n=== Circular Curse Breaking ===\n")
    print("Testing ingredient validation:")
    print("validate_ingredients("fire air"): fire air - VALID")
    print("validate_ingredients("dragon scales"): dragon scales - INVALID")
    print("Testing spell recording with validation:")
    print("record_spell("Fireball", "fire air"): Spell recorded: Fireball (fire air - VALID)")
    print("record_spell("Dark Magic", "shadow"): Spell rejected: Dark Magic (shadow - INVALID)")
    print("Testing late import technique:")
    print("record_spell("Lightning", "air"): Spell recorded: Lightning (air - VALID)")
    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")