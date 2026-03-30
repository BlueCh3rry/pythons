def ft_harvest_total() -> None:
    x = int(input("Day 1 harvest: "))
    y = int(input("Day 2 harvest: "))
    z = int(input("Day 3 harvest: "))
    result: int = y + x + z
    print("Total harvest:", result)
