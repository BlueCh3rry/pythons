import sys


def invent_init() -> dict:
    inventory = {}
    if len(sys.argv) == 1:
        raise ValueError("No object provided.")
    for arg in sys.argv[1:]:
        parts = arg.split()
        for part in parts:
            if ':' in part:
                name, qty_str = part.split(':', 1)
                try:
                    if name not in inventory:
                        inventory[name] = int(qty_str)
                    else:
                        print(f"Redundant item '{name}' - discarding")
                except ValueError as e:
                    print(f"Error: Invalid quantity for '{name}': {e}\n")
            else:
                print(f"Error - invalid parameter '{part}'")
    return inventory


def count_quantity(inventory: dict) -> int:
    count = 0
    for name, quantity in inventory.items():
        count += int(quantity)
    return count


def count_items(inventory: dict) -> int:
    count = 0
    for name in inventory.items():
        count += 1
    return count


def current_invent(inventory: dict) -> None:
    for name, qty in inventory.items():
        usage = qty/count_quantity(inventory)*100
        print(f"Item {name} represents {'%.2f' % usage}%")
    print()


def invent_analysis(inventory: dict):
    name_list = []
    for name, qty in inventory.items():
        name_list.append(name)
    print(f"Got inventory: {inventory.items()}")
    print(f"Item list: {name_list}")
    items = count_items(inventory)
    count = count_quantity(inventory)
    print(f"Total quantity of the {items} items: {count}\n")


def invent_stats(inventory: dict) -> None:
    first = next(iter(inventory))
    name_lowest = name_highest = first
    qty_highest = qty_lowest = inventory[first]
    for name, qty in inventory.items():
        if qty < qty_lowest:
            qty_lowest = qty
            name_lowest = name
        if qty > qty_highest:
            qty_highest = qty
            name_highest = name
    print(f"Item most abundant: {name_highest} with quantity {qty_highest}")
    print(f"Item least abundant: {name_lowest} with quantity {qty_lowest}\n")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = invent_init()
    invent_analysis(inventory)

    current_invent(inventory)
    invent_stats(inventory)


if __name__ == "__main__":
    main()
