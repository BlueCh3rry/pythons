from enum import Enum
import random
from typing import TypedDict
from colorama import Fore


class Direction(Enum):
    """Represent the direction offset

    Attributes:
        NORTH: First bit (LSB)
        EAST: Second bit
        SOUTH: Third bit
        WEST: Fourth bit
    """

    WEST = 0
    SOUTH = 1
    EAST = 2
    NORTH = 3


class LocalData(TypedDict):
    """Type of local_visited dictionnary

    Attributes:
        direction (Direction): The direction of the neighboor
        from the current cell
        coordinates (tuple[int, int]): The coordinates of the cell
        (The neighboor of the current cell)
    """

    direction: Direction
    coordinates: tuple[int, int]


class MazeGenerator:
    """A maze manager capable of generate a random maze.

    This class handle the generation of the maze from a seed,
    including the 42 logo.

    Args:
        width (int): The width of the maze. Must be greater or equal to 1
        height (int): The hight of the maze. Must be greater or equal to 1
        seed (int): The seed of the maze
        entry (tuple[int, int]): A couple of coordinates that represent
            the entrance of the maze
        exit (tuple[int, int]): A couple of coordinates that represent
            the entrance of the maze

    Attributes:
        solution (list[tuple[int, int]]): The list of visited cells during
            the solving execution
        path (dict[tuple[int, int], tuple[tuple[int, int] | None, str]]):
            The list of visited cells during the solving execution
            and their direction from the entrance
        maze (list[list[str]]): The binary representation of the maze
        visited (list[tuple[int, int]]): The visited cells
        forty_two_cell (list[tuple[int, int]]): The list of the cells
            from the 42 logo
        add_forty_two (bool): If the forty fit in the maze

    Notes:
        To access to the solution path, you must used the parsing method
        that take the result of the solve function
    """

    def __init__(
        self,
        width: int,
        height: int,
        seed: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
    ) -> None:
        self.width = width
        self.height = height
        self.seed = seed
        self.entry: tuple[int, int] = entry
        self.exit: tuple[int, int] = exit
        self.solution: list[tuple[int, int]] = []
        self.path: dict[
            tuple[int, int], tuple[tuple[int, int] | None, str]
        ] = {}
        random.seed(self.seed)
        self.maze: list[list[str]] = [
            ["1111" for _ in range(self.width)] for _ in range(self.height)
        ]
        self.visited: list[tuple[int, int]] = []
        self.forty_two_cell = self.generate_forty_two()
        self.add_forty_two = True
        for x, y in self.forty_two_cell:
            if x < 0 or y < 0:
                print("Error: 42 logo is too large for the maze")
                self.add_forty_two = False
                break
        if self.entry in self.forty_two_cell and self.add_forty_two:
            raise ValueError(
                "Error: the entrance cannot be "
                "at the same place as the 42 logo"
            )
        if self.exit in self.forty_two_cell and self.add_forty_two:
            raise ValueError(
                "Error: the exit cannot be at the same place as the 42 logo"
            )
        if self.add_forty_two:
            self.visited += self.forty_two_cell

    def generate(self, coordinates: tuple[int, int]) -> None:
        """Generate a maze

        Generate a maze from a seed using a backtracking algorithm.

        Args:
            coordinates (tuple[int, int]): A coordinate pair (x, y)
        """
        local_not_visited: list[LocalData] = [
            {
                "direction": Direction.NORTH,
                "coordinates": (coordinates[0], coordinates[1] - 1),
            },
            {
                "direction": Direction.EAST,
                "coordinates": (coordinates[0] + 1, coordinates[1]),
            },
            {
                "direction": Direction.SOUTH,
                "coordinates": (coordinates[0], coordinates[1] + 1),
            },
            {
                "direction": Direction.WEST,
                "coordinates": (coordinates[0] - 1, coordinates[1]),
            },
        ]
        if coordinates not in self.visited:
            if (
                self.is_in_maze(self.width, self.height, coordinates)
                or coordinates is self.entry
            ):
                self.visited.append(coordinates)
                while local_not_visited:
                    res = random.randint(0, len(local_not_visited) - 1)
                    direction = local_not_visited[res]["direction"]
                    coords = local_not_visited[res]["coordinates"]
                    if not (coords in self.visited) and self.is_in_maze(
                        self.width, self.height, coords
                    ):
                        self.update_cell(coordinates, direction)
                        self.update_cell(
                            coords, Direction((direction.value + 2) % 4)
                        )
                        self.generate(coords)
                    local_not_visited.pop(res)

    def dig(self, probability: float = 0.1) -> None:
        """Break some walls to make multiple path to the exit

        Break the walls with a custom probability for the settings
        perfect=False

        Arguments:
            probability (float): The probability that the wall will break.
            If higher the probability, the greater the chance that the wall
            will break
        """
        for y in range(self.height):
            for x in range(self.width):
                for i in range(4):
                    if x == 0 and i == 0:
                        # West walls of the left cells cannot be broken
                        continue
                    if x == self.width - 1 and i == 2:
                        # East walls of the right cells cannot be broken
                        continue
                    if y == 0 and i == 3:
                        # North walls of the top cells cannot be broken
                        continue
                    if y == self.height - 1 and i == 1:
                        # South walls of the bottom cells cannot be broken
                        continue
                    if (x, y) in self.forty_two_cell:
                        continue
                    if random.randint(0, 100) / 100 <= probability:
                        if i == 0:
                            if (x - 1, y) not in self.forty_two_cell:
                                self.update_cell((x, y), Direction(i))
                                self.update_cell((x - 1, y), Direction(2))
                        if i == 1:
                            if (x, y + 1) not in self.forty_two_cell:
                                self.update_cell((x, y), Direction(i))
                                self.update_cell((x, y + 1), Direction(3))
                        if i == 2:
                            if (x + 1, y) not in self.forty_two_cell:
                                self.update_cell((x, y), Direction(i))
                                self.update_cell((x + 1, y), Direction(0))
                        if i == 3:
                            if (x, y - 1) not in self.forty_two_cell:
                                self.update_cell((x, y), Direction(i))
                                self.update_cell((x, y - 1), Direction(1))

    def update_cell(
        self, coordinates: tuple[int, int], direction: Direction
    ) -> bool:
        """Update the cell value

        This method updates the cell based on the direction
        (converted to an offset to modify the binary value)

        Args:
            coordinates (tuple[int, int]): A couple of coordinates
            direction (Direction): An instance of Direction enum
            (can be converted in number)

        Returns:
            bool: True if the cell has been successfully modified,
            false otherwise
        """
        try:
            temp = list(self.maze[coordinates[1]][coordinates[0]])
            temp[direction.value] = "0"
            self.maze[coordinates[1]][coordinates[0]] = "".join(temp)
            return True
        except Exception:
            return False

    def solve(
        self,
    ) -> dict[tuple[int, int], tuple[tuple[int, int] | None, str]]:
        """Solve the generated maze

        Use the BFS algorithm to solve the generated maze (stored as self.maze)

        Returns:
            dict[str, tuple[tuple[int, int], Direction]]: A dictionary that can
            be used like a chained list
            It contains all tried paths from the entrance to the exit.
            Note: This output has to be parsed.
        """
        queue = [self.entry]
        visited = []

        path: dict[tuple[int, int], tuple[tuple[int, int] | None, str]] = {
            self.entry: (None, str(""))
        }

        while queue:
            if queue[0] == self.exit:
                break
            coords = queue.pop(0)
            visited.append(coords)
            neighbors: list[LocalData] = [
                {
                    "direction": Direction.WEST,
                    "coordinates": (coords[0] - 1, coords[1]),
                },
                {
                    "direction": Direction.SOUTH,
                    "coordinates": (coords[0], coords[1] + 1),
                },
                {
                    "direction": Direction.EAST,
                    "coordinates": (coords[0] + 1, coords[1]),
                },
                {
                    "direction": Direction.NORTH,
                    "coordinates": (coords[0], coords[1] - 1),
                },
            ]
            for neighbor in neighbors:
                if (
                    self.is_in_maze(
                        self.width, self.height, neighbor["coordinates"]
                    )
                    and neighbor["coordinates"] not in visited
                    and list(self.maze[coords[1]][coords[0]])[
                        neighbor["direction"].value
                    ]
                    == "0"
                ):
                    queue.append(neighbor["coordinates"])
                    visited.append(neighbor["coordinates"])
                    path[neighbor["coordinates"]] = (
                        coords,
                        neighbor["direction"].name[0],
                    )
        self.path = path
        return path

    def parser(
        self, path: dict[tuple[int, int], tuple[tuple[int, int] | None, str]]
    ) -> str:
        """The solution parser

        Convert the path returned by solve() in string.
        It begin a the exit and go back to the entrance.
        The dictionary is like a chained list.

        Returns:
            str: The reversed solution
        """
        current: tuple[int, int] | None = self.exit
        formated_output = ""
        while current:
            self.solution.append(current)
            formated_output += path[current][1]
            current = path[current][0]
        return formated_output[::-1]

    @staticmethod
    def is_in_maze(
        width: int, height: int, coordinates: tuple[int, int]
    ) -> bool:
        """Function validation for a cell

        Check whether the transmitted cell is within the dimensions
        of the maze

        Args:
            width (int): The width of the maze
            height (int): The height of the maze
            coordinates (tuple[int, int]): A couple of coordinates

        Returns:
            bool: True if the cell is in the maze, False otherwise
        """
        if (
            coordinates[0] < width
            and coordinates[1] < height
            and coordinates[0] >= 0
            and coordinates[1] >= 0
        ):
            return True
        return False

    def generate_forty_two(self) -> list[tuple[int, int]]:
        """Add the 42 logo to the maze

        Center the 42 logo cells with a simple formula:
        (size of the container - size of the logo) // 2 for x and y axis

        Returns:
            list[tuple[int, int]]: A list of coordinates couple
        """
        cell_list = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 2),
            (2, 2),
            (2, 3),
            (2, 4),
            (4, 0),
            (5, 0),
            (6, 0),
            (6, 1),
            (6, 2),
            (5, 2),
            (4, 2),
            (4, 3),
            (4, 4),
            (5, 4),
            (6, 4),
        ]
        cell_modified: list[tuple[int, int]] = [
            (cell[0] + (self.width - 7) // 2, cell[1] + (self.height - 5) // 2)
            for cell in cell_list
        ]

        return cell_modified

    def print_output(self, color_list: list[str], color: int) -> None:
        """Generate the ascii representation of the maze

        This method merges the cell walls for a clear output.
        In addition, it marks the entry and the exist with E and X characters

        Returns:
            str: The maze formatted with \\n for new lines
        """
        rows = self.height * 2 + 1
        cols = self.width * 2 + 1
        grid = [
            [f"{color_list[color]}█" for _ in range(cols)] for _ in range(rows)
        ]
        for y in range(self.height):
            for x in range(self.width):
                cy, cx = y * 2 + 1, x * 2 + 1
                grid[cy][cx] = " "
                val = self.maze[y][x]
                if val[3] == "0":
                    grid[cy - 1][cx] = " "
                if val[2] == "0":
                    grid[cy][cx + 1] = " "
                if val[1] == "0":
                    grid[cy + 1][cx] = " "
                if val[0] == "0":
                    grid[cy][cx - 1] = " "
                if (x, y) in self.forty_two_cell and self.add_forty_two:
                    grid[cy][cx] = f"{Fore.LIGHTBLUE_EX}█"
                if (x, y) == self.entry:
                    grid[cy][cx] = f"{Fore.GREEN}█"
        for y in range(self.height):
            for x in range(self.width):
                cy, cx = y * 2 + 1, x * 2 + 1
                if (x, y) in self.solution and (x, y) != self.entry:
                    grid[cy][cx] = f"{Fore.LIGHTMAGENTA_EX}█"
                    if self.path[(x, y)][1] == "N":
                        grid[cy + 1][cx] = f"{Fore.LIGHTMAGENTA_EX}█"
                    if self.path[(x, y)][1] == "S":
                        grid[cy - 1][cx] = f"{Fore.LIGHTMAGENTA_EX}█"
                    if self.path[(x, y)][1] == "E":
                        grid[cy][cx - 1] = f"{Fore.LIGHTMAGENTA_EX}█"
                    if self.path[(x, y)][1] == "W":
                        grid[cy][cx + 1] = f"{Fore.LIGHTMAGENTA_EX}█"
                if (x, y) == self.exit:
                    grid[cy][cx] = f"{Fore.LIGHTRED_EX}█"
        print("\n".join("".join(row) for row in grid))
