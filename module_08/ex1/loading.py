import sys
import importlib
import pandas
import numpy
import matplotlib.pyplot as plt  # type: ignore


AUTHORIZED = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "requests": "Network access",
    "matplotlib": "Visualization",
}


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
    for name, version in dependencies:
        if name in AUTHORIZED:
            description = AUTHORIZED[name]
            print(f"[OK] {name} ({version}) - {description} ready")
        else:
            print(f"[ERROR] {name} ({version}) - unauthorized package")

    verify_missing(dependencies, file)


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")

    print("\nChecking dependencies:")
    data = "/home/mmakhmae/42cursus/pythons/module_08/ex1/requirements.txt"
    data2 = "/home/mmakhmae/42cursus/pythons/module_08/ex1/pyproject.toml"
    


    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    matrix = numpy.random.normal(size=1000)
    print("Generating visualization...")
    df = pandas.DataFrame(matrix, columns=["values"])
    matplotlib.pyplot.hist(df["values"], bins=30)
    matplotlib.pyplot.title("Matrix Data Distribution")
    matplotlib.pyplot.savefig(
        "/home/mmakhmae/42cursus/pythons/module_08/ex1/matrix_analysis.png")
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
