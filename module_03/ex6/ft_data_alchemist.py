import random


def score_dict(lst: list) -> dict:
    return {elm: random.randint(0, 999) for elm in lst}


def main():
    print("=== Game Data Alchemist ===\n")
    lst = [
        "Alice", "bob", "Charlie",
        "dylan", "Emma", "Gregory",
        "john", "kevin", "Liam"
    ]
    print("Initial list of players", lst)

    lst_C = [elm.capitalize() for elm in lst]
    print("New list with all names capitalized:", lst_C)

    lst_t = [elm for elm in lst if elm == elm.capitalize()]
    print("New list of capitalized names only:", lst_t)
    print()

    dico = score_dict(lst_C)
    print("Score dict", dico)
    average = round(sum(dico.values()) / len(dico), 2)
    print("Score average is:", average)

    dico_h = {name: qty for name, qty in dico.items() if qty > average}
    print(f"High scores: {dico_h}")


if __name__ == "__main__":
    main()
