import importlib


pandas = importlib.import_module("pandas")
numpy = importlib.import_module("numpy")
plt = importlib.import_module("matplotlib.pyplot")


AUTHORIZED = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "requests": "Network access",
    "matplotlib": "Visualization",
}


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


def read_dependencies(path: str) -> list[tuple[str, str]]:
    dependencies = []
    data = pandas.read_csv(path, header=None)
    for raw_line in data[0]:
        line = raw_line.strip()
        if "==" not in line:
            continue
        line = line.replace('"', "")
        line = line.replace(",", "")
        dependency = line.split("#")[0].strip()
        name, version = dependency.split("==", 1)
        dependencies.append((name.strip(), version.strip()))
    return dependencies


def verify_missing(installed: list[str], file: str) -> None:
    for package in AUTHORIZED:
        if package not in installed:
            print(f"[ERROR - MISSING in {file}] {package}")


def check_dep(path: str, file: str) -> None:
    dependencies = read_dependencies(path)
    installed = []
    for name, version in dependencies:
        if name in AUTHORIZED:
            description = AUTHORIZED[name]
            installed.append(name)
            print(f"[OK] {name} ({version}) - {description} ready")
        else:
            print(f"[ERROR] {name} ({version}) - unauthorized package")
    verify_missing(installed, file)


def main() -> None:

    print("\nLOADING STATUS: Loading programs...")

    print("\nChecking dependencies:")
    data = "/home/mmakhmae/42cursus/pythons/module_08/ex1/requirements.txt"
    data2 = "/home/mmakhmae/42cursus/pythons/module_08/ex1/pyproject.toml"

    check_dep(data, "requirements.txt")
    # check_dep(data2, "pyproject.toml")

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    matrix = numpy.random.normal(size=1000)
    print("Generating visualization...")
    df = pandas.DataFrame(matrix, columns=["values"])
    plt.hist(df["values"], bins=30)
    plt.title("Matrix Data Distribution")
    plt.savefig(
        "/home/mmakhmae/42cursus/pythons/module_08/ex1/matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
