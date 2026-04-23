import alchemy.grimoire


def main() -> None:
    print("=== Kaboum 0 ===")
    print("Using grimoire module directly")
    ing = "Earth, wind and fire"
    print("Testing record light spell:",
          alchemy.grimoire.light_spell_record("Fantsasy", ing))


if __name__ == "__main__":
    main()
