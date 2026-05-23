#!/usr/bin/python3


def mage_counter() -> callable:
    counter = 0

    def count() -> int:
        nonlocal counter
        counter += 1
        return counter

    return count


def spell_accumulator(initial_power: int) -> callable:
    accumulation = initial_power

    def get_accumulation(amount: int) -> int:
        nonlocal accumulation
        accumulation += amount
        return accumulation

    return get_accumulation


def enchantment_factory(enchantment_type: str) -> callable:
    etype = enchantment_type

    def enchanter(item_name: str) -> str:
        return f"{etype} {item_name}"

    return enchanter


def memory_vault() -> dict[str, callable]:
    dictionnary = {}

    def store(key: str, value: any) -> None:
        dictionnary[key] = value
        return None

    def recall(key: str) -> any:
        if key in dictionnary.keys():
            return dictionnary[key]
        else:
            return "Memory not found"

    return {"store": store, "recall": recall}


def main() -> None:
    print("Testing mage counter...")
    function = mage_counter()
    print(f"Call 1: {function()}")
    print(f"Call 2: {function()}")
    print(f"Call 3: {function()}")
    print("")

    print("Testing spell accumulator (base 50)...")
    accumulation = spell_accumulator(50)
    print(accumulation(3))
    print(accumulation(3))
    print(accumulation(3))
    print("")

    print("Testing enchantment factory...")
    fire = enchantment_factory("Flaming")
    ice = enchantment_factory("Frozen")
    print(fire("sword"))
    print(fire("ball"))
    print(ice("sword"))
    print(ice("ball"))
    print("")

    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("secret_key", 4242)
    print(vault["recall"]("secret_key"))
    print("")
    return None


if __name__ == "__main__":
    main()
