from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter
    return count


def spell_accumulator(initial_power: int) -> Callable:
    accumulation = initial_power

    def get_accumulation(amount: int) -> int:
        nonlocal accumulation
        accumulation += amount
        return accumulation
    return get_accumulation


def enchantment_factory(enchantment_type: str) -> Callable:
    etype = enchantment_type

    def enchanter(item_name: str) -> str:
        return f"{etype} {item_name}"
    return enchanter


def memory_vault() -> dict[str, Callable]:
    dictionnary = {}

    def store(key: str, value: Any) -> None:
        dictionnary[key] = value
        return None

    def recall(key: str) -> Any:
        if key in dictionnary.keys():
            return dictionnary[key]
        else:
            return "Memory not found"
    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print()

    print("Testing spell accumulator...")
    accumulation = spell_accumulator(100)
    print("Base 100, add 20:", accumulation(20))
    print("Base 100, add 30:", accumulation(30))
    print()

    print("Testing enchantment factory...")
    fire = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")
    print(fire("Sword"))
    print(ice("Shield"))
    print()

    print("Testing memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret_key", 42)
    print("Recall 'secret':", vault["recall"]("secret_key"))
    print("Recall 'unknown':", vault["recall"]("unknown"))
    print()


if __name__ == "__main__":
    main()
