from alchemy.potions import strength_potion, healing_potion


def main():
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    print(f"Testing strength_potion: {strength_potion()}")
    print(f"Testing healing_potion: {healing_potion()}\n")


if __name__ == "__main__":
    main()
