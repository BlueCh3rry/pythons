def ft_count_harvest_iterative() -> None:
    x = int(input("Days until harvest: "))
    for count in range(1, x + 1):
        print("Day:", count)
        if (count == x):
            print("Harvest time!")
