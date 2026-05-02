*This project has been created as part of the 42 curriculum by kmathuri, rstrcic*

# Description
The goal of this project is to generate a random maze and solving it.

Features:
- Custom configuration (width, height...)
- Default configuration file
- Seed system (permit reproducibility)
- Generating algorithm (backtracking)
- Show 42 logo in the center of the maze
- Solving algorithm (using BFS)
- TUI interface:
	- Regenerate maze
	- Hide/Show solving path
	- Rotate color
- Error handling
- Makefile (auto install poetry)
- Output file containing hexadecimal representation of the maze, the entrance and the exit and the solving path

## Output format
In "output_file.txt":
```text
<hexadecimal representation of the maze>

<Entrance coordinates>
<Exit coordinates>
<Cardinal direction string for the solving path>
```
## Config file structure
```text
in "config.txt":
    - WIDTH=<int> > 1
    - HEIGHT=<int> > 1
    - ENTRY=<tuple> >= 0
    - EXIT=<tuple> >= 0
    - OUTPUT_FILE=<string>
    - PERFECT=True or PERFECT=False
optional parameter:
    - SEED=<int>
```

## Algorithms
For generation: Backtracking. We chose it because it was the more logical for us.
For solving: BFS (Breadth First Search). It was a good compromise between logic and performance.

## Reusable part
- MazeGenerator class
    This class handle the generation of the maze from a seed,
    including the 42 logo.
```python
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
```
- Output generation system
```python
    Generate the hexadecimal view of the maze,
    the coordinates of the entrance and exit
    and the path from the entrance to the exit

    Arguments:
        filename (str): The path to the config file
        maze (MazeGenerator): The binary representation of the maze
        entry (tuple[int, int]): The coordinates of the entry
        exit (tuple[int, int]): The coordinates of the exit
```
## Project management
### Roles
- kmathuri:
	- Solving algorithm
	- Makefile
	- Parsing
	- File structure
	- Error handling
	- Docstrings
- rstrcic:
	- Generation algorithm
	- Output file
	- TUI
	- Testing
	- Docstrings
### Planning
- Atomic task structure
- The tasks became clearer as time went on
### What worked well
- Git system
- Good communication
- Synchronised presence
### What can be improved
- Task breakdown
### Tools
- We used Linear to make Todo and issues synchronised with our git repository
- We used Github project to review the code of each other

# Instructions
## Installation
```bash
make install
```
## Debug
```bash
make debug
```
## Run
```bash
make run
```
## Lint
For simple linting:
```bash
make lint
```
For strict linting:
```bash
make lint-strict
```
## Remove cache files
```bash
make clean
```
## Build module
```bash
poetry build
```
## Install module
```bash
poetry add <module_name>
poetry install
```


# Resources
https://www.geeksforgeeks.org/python/print-colors-python-terminal/
https://docs.pydantic.dev/latest/
https://pypi.org/project/python-dotenv/
https://python-poetry.org/docs/#installing-with-the-official-installer
https://www.w3schools.com/python/ref_list_pop.asp
The AI was used to understand algorithm and to ask about the subject
