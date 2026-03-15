import sys


def demo():
    pass


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
                    inventory[name] = int(qty_str)
                except ValueError:
                    raise ValueError(f"Error: Invalid quantity for {name}.\n")
            else:
                raise SyntaxError(f"Invalid 'name:number' format, got: {part}")
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
    print("=== Current Inventory ===")
    for name, qty in inventory.items():
        usage = qty/count_quantity(inventory)*100
        print(f"{name}: {qty} units ({'%.2f' % usage}%)")
    print()


def invent_stats(inventory: dict) -> None:
    print("=== Inventory Statistics ===")
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
    print(f"Most abundant: {name_highest} ({qty_highest} units)")
    print(f"Most abundant: {name_lowest} ({qty_lowest} units)\n")


def invent_analysis(inventory: dict):
    print("=== Inventory System Analysis ===")
    count = count_quantity(inventory)
    print(f"Total items in inventory: {count}")
    items = count_items(inventory)
    print(f"Unique item types: {items}\n")


def main() -> None:
    inventory = invent_init()
    invent_analysis(inventory)
    current_invent(inventory)
    invent_stats(inventory)

    print("=== Item Categories ===")

    print("=== Management Suggestions ===")

    print("=== Dictionary Properties Demo ===")
    name_list = []
    for name, qty in inventory.items():
        name_list.append(name)
    qty_list = [inventory[name] for name in inventory.keys()]
    print(name_list)
    print(qty_list)


if __name__ == "__main__":
    main()
