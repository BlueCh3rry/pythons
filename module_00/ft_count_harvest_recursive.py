def ft_recu(count, x):
    if (count != x + 1):
        print("Day:", count)
        ft_recu(count + 1, x)

def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))
    count = int(1)
    ft_recu(count, x)
    print("Harvest time!")
