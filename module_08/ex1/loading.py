import pandas
import numpy
import matplotlib.pyplot


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    Req = ["pandas", "numpy", "requests", "matplotlib"]
    Installed = []

    data = pandas.read_csv(
        "/home/mmakhmae/42cursus/pythons/module_08/ex1/requirements.txt",
        header=None)
    for line in data[0]:
        if '#' in line:
            dependecie, comment = line.split("#")
            name, version = dependecie.split("==")
            Installed.append(name)
            if name in Req:
                print(f"[OK] {name} ({version.strip()}) -",
                      f"{comment.strip()} ready")
            else:
                print(f"[ERROR] {name} ({version.strip()}) -",
                      f" {comment.strip()} is wrong")
    i = 0
    while i < len(Req):
        if Req[i] not in Installed:
            print("[ERROR - MISSING]", Req[i])
        i += 1

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    matrix = numpy.random.normal(size=1000)
    print("Generating visualization...")
    df = pandas.DataFrame(matrix, columns=["values"])
    matplotlib.pyplot.hist(df["values"], bins=30)
    matplotlib.pyplot.title("Matrix Data Distribution")
    matplotlib.pyplot.savefig(
        "/home/mmakhmae/42cursus/pythons/module_08/ex1/matrix_analysis.png")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
