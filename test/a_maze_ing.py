try:
    from random import randint
    import sys
    from typing import Tuple, TypedDict, Union
    from pydantic import BaseModel, Field, ValidationError, model_validator
    from colorama import Fore
    from mazegen.generator import MazeGenerator
    import dotenv
except ImportError as e:
    print(f"ERROR: {e}")
    exit()


def generate_seed() -> int:
    """Generate a random seed

    Generate a formated seed between 1000000 and 9999999.
    It's an arbitrary range, just for good visual.

    Returns:
        int: The generated seed
    """
    return randint(1000000, 9999999)


class Config(BaseModel):
    """Validation model of the config file

    Attributes:
        width (int): The width of the maze. Must be greater or equal to 1
        height (int): The hight of the maze. Must be greater or equal to 1
        entry (tuple[int, int]): A couple of coordinates that represent
        the entrance of the maze
        exit (tuple[int, int]): A couple of coordinates that represent
        the entrance of the maze
        output_file (str): The path to the output file
        perfect (bool): Change if the maze will have only one path to the exit
        seed (int): The seed of the maze
    """

    width: int = Field(ge=1)
    height: int = Field(ge=1)
    entry: Tuple[int, int]
    exit: Tuple[int, int]
    output_file: str = Field(min_length=1)
    perfect: bool
    seed: int = Field(default_factory=generate_seed)

    @model_validator(mode="after")
    def checker(self: "Config") -> "Config":
        """Custom validation applicated to the config file

        raises:
            ValueError: In the following cases:
                - If the maze entrance and exit are outside the dimensions
                of the maze
                - If the maze entrance and exit are at the same coordinates
        """
        if (
            self.entry[0] < 0
            or self.entry[0] > self.width - 1
            or self.entry[1] < 0
            or self.entry[1] > self.height - 1
        ):
            raise ValueError("Invalid entry coordinates")
        if (
            self.exit[0] < 0
            or self.exit[0] > self.width - 1
            or self.exit[1] < 0
            or self.exit[1] > self.height - 1
        ):
            raise ValueError("Invalid exit coordinates")
        if self.exit == self.entry:
            raise ValueError("Entry and exit cannot be at the same place")
        return self


class ConfigData(TypedDict, total=False):
    """The args type dictionary

    This dictionary type help for mypy errors

    width (int): The width of the maze. Must be greater or equal to 1
    height (int): The hight of the maze. Must be greater or equal to 1
    entry (tuple[int, int]): A couple of coordinates that represent
    the entrance of the maze
    exit (tuple[int, int]): A couple of coordinates that represent
    the entrance of the maze
    output_file (str): The path to the output file
    perfect (bool): Change if the maze will have only one path to the exit
    seed (int): The seed of the maze
    """

    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int


def parsing(config_file: str) -> Union[Config, None]:
    """Parse the config file

    Parse and validate if the file is correctly formed using Config base model.
    It load the file using dotenv

    Args:
        config_file (str): The path to the config file

    Returns:
        None: If the file is not properly configured
        Config: If the file passed all of the verifications
    """
    path = dotenv.find_dotenv(config_file)
    if not path:
        raise FileNotFoundError(f"Error: {config_file} file not found")
    config = dotenv.dotenv_values(config_file)
    args: ConfigData = {}
    for key, value in config.items():
        if key.startswith("#"):
            continue
        key = key.upper()
        if value is not None:
            if key == "WIDTH":
                args["width"] = int(value)
            elif key == "HEIGHT":
                args["height"] = int(value)
            elif key == "ENTRY" or key == "EXIT":
                splited_value = value.split(",")
                converted_to_tuple: tuple[int, int] = (
                    int(splited_value[0]),
                    int(splited_value[1]),
                )
                if key == "ENTRY":
                    args["entry"] = converted_to_tuple
                else:
                    args["exit"] = converted_to_tuple
            elif key == "OUTPUT_FILE":
                args["output_file"] = value
            elif key == "PERFECT":
                if value == "True":
                    args["perfect"] = True
                if value == "False":
                    args["perfect"] = False
            elif key == "SEED":
                args["seed"] = int(value)
            else:
                raise ValueError("Error: Unknown key")
        else:
            raise ValueError("Error: Config file malformed")
    ctx = Config(**args)
    return ctx


def generate_output_file(
    filename: str,
    maze: MazeGenerator,
    entry: tuple[int, int],
    exit: tuple[int, int],
) -> None:
    """Generate the output file

    Generate the hexadecimal view of the maze,
    the coordinates of the entrance and exit
    and the path from the entrance to the exit

    Arguments:
        filename (str): The path to the config file
        maze (MazeGenerator): The binary representation of the maze
        entry (tuple[int, int]): The coordinates of the entry
        exit (tuple[int, int]): The coordinates of the exit
    """
    content = ""
    for row in maze.maze:
        for cell in row:
            content += str(hex(int(cell, 2))).replace("0x", "").upper()
        content += "\n"
    with open(filename, "w") as f:
        f.write(content)
        f.write("\n")
        f.write(str(entry).replace("(", "").replace(")", "").replace(" ", ""))
        f.write("\n")
        f.write(str(exit).replace("(", "").replace(")", "").replace(" ", ""))
        f.write("\n")
        f.write(maze.parser(maze.solve()))
        f.write("\n")


color_list = [
    Fore.BLUE,
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTCYAN_EX,
    Fore.MAGENTA,
    Fore.WHITE,
    Fore.LIGHTYELLOW_EX,
]


def generate_maze(
    show_solution: bool, seed: int | None, offset: int = 0, error: bool = False
) -> None:
    """Generate the maze and show the TUI

    Arguments:
        show_solution (bool): True if the solution path is visible,
            false otherwise
        seed (int | None): An int if we want the same maze as before,
            none otherwise.
        error (bool = False): True if there is an error (unknown parameter),
            False otherwise
    """
    try:
        ctx = parsing(sys.argv[1])
    except ValidationError as e:
        print(e.errors()[0]["msg"], e.errors()[0]["loc"])
        return
    except ValueError as e:
        print(e)
        return
    except (FileNotFoundError, PermissionError) as e:
        print(e)
        return
    except Exception as e:
        print("Error: Config file error:", e)
        return
    if isinstance(ctx, Config):
        if seed:
            ctx.seed = seed
        try:
            maze = MazeGenerator(
                width=ctx.width,
                height=ctx.height,
                seed=ctx.seed,
                entry=ctx.entry,
                exit=ctx.exit,
            )
            maze.generate(ctx.entry)
            if not ctx.perfect:
                maze.dig(0.1)
            if show_solution:
                maze.parser(maze.solve())
            maze.print_output(color_list, offset)
            if error:
                print(Fore.RED + "Error: Unknown parameter")
            generate_output_file(ctx.output_file, maze, ctx.entry, ctx.exit)
            print(Fore.RESET + "=== A-Maze-ing ===")
            print("1. Re-generate a new maze")
            print("2. Show/Hide path from entry to exit")
            print("3. Rotate maze colors")
            print("4. Quit")
            try:
                param = input("Choice? (1-4): ")
                if param == "1":
                    generate_maze(show_solution, None, offset)
                elif param == "2":
                    generate_maze(not (show_solution), ctx.seed, offset)
                elif param == "3":
                    generate_maze(
                        show_solution,
                        ctx.seed,
                        (offset + 1) % (len(color_list)),
                    )
                elif param == "4":
                    return
                else:
                    generate_maze(show_solution, ctx.seed, offset, True)
            except KeyboardInterrupt:
                print("\nExiting...")
                exit()
        except RecursionError:
            print(
                "Error: Maze too large. "
                "The algorithm reach python recursion limit"
            )
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print(
            "Error: Invalid arguments. Usage: python3 a_maze_ing.py config.txt"
        )
    else:
        generate_maze(True, None)
