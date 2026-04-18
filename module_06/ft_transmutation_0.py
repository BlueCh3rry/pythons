import alchemy.transmutation


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    print("Testing lead to gold:",
          alchemy.transmutation.recipes.lead_to_gold())
    print()


if __name__ == "__main__":
    main()
