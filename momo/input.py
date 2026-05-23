from colorama import Fore
from enum import Enum
from maze_map import Cell


class Color(Enum):
    Fore.BLACK
    Fore.WHITE
    Fore.MAGENTA
    Fore.RED
    Fore.BLUE
    Fore.GREEN
    Fore.YELLOW
    Fore.RESET


def ui() -> None:
    txt = ("=== a-maze-ing ===\n"
           "1. Re-generate a new maze\n"
           "2. Show/Hide path from entry to exit\n"
           "3. Rotate maze colors\n"
           "4. Quit")
    print(txt)
    try:
        param = input("Choice? (1-4): ")
        while param != "4":
            if param == "1":
                print("111111111111111111111111111111111111")
            elif param == "2":
                print("222222222222222222222222222222222222")
            elif param == "3":
                print("333333333333333333333333333333333333")
            else:
                print("Invalid input, Quiting...")
                return
            print(txt)
            param = input("Choice? (1-4): ")
    except KeyboardInterrupt:
        print("\nError input, Quiting...")
        exit()


def color_map(maze: list[list[Cell]]) -> None:
    for row in maze:
        for cell in row:
            if cell.is_exit:
                pass
            if cell.is_start:
                pass
            if cell.is_ft:
                pass
            if cell.:
                pass


if __name__ == "__main__":
    ui()
