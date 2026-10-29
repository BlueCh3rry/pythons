import importlib
from importlib.metadata import version


"""
pip setup:
pip freeze > requirements.txt
to use to reinstall a setup in the existing venv
pip install -r requirements.txt

poetry setup:
create .toml
python3 -m poetry init --no-interaction
fill .toml
python3 -m poetry add "numpy<2.0" matplotlib "pandas<3.0"
use .toml to create pseudo venv
python3 -m poetry install --no-root
use .loading
python3 -m poetry run python loading.py
"""


def get_dependecy(name: str) -> bool:
    try:
        importlib.import_module(name)
        return True
    except ImportError:
        return False


def get_version(name: str) -> str | None:
    try:
        return version(name)
    except ImportError:
        return None


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    Req = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization",
    }
    for name in Req:
        if get_dependecy(name) is True:
            if get_version(name) is not None:
                print(f"[OK] {name} {get_version(name)}- {Req[name]}")

    pandas = importlib.import_module("pandas")
    numpy = importlib.import_module("numpy")
    plt = importlib.import_module("matplotlib.pyplot")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    matrix = numpy.random.normal(size=1000)
    print("Generating visualization...")
    df = pandas.DataFrame(matrix, columns=["values"])
    plt.hist(df["values"], bins=30)
    plt.title("Matrix Data Distribution")
    # plt.savefig(
    #     "/home/mmakhmae/42cursus/pythons/module_08/ex1/matrix_analysis.png")
    plt.savefig(
        "C:/Users/Red/home/42cursus/pythons/module_08/ex1/matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
