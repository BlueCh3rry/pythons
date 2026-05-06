import pandas
# import numpy
# import matplotlib


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")
    print("\nChecking dependencies:")
    Req = ["pandas", "numpy", "requests", "matplotlib"]
    data = pandas.read_csv(
        "/home/mmakhmae/42cursus/pythons/module_08/ex1/requirements.txt",
        header=None)
    for line in data[0]:
        if '#' in line:
            dependecie, comment = line.split("#")
            name, version = dependecie.split("==")
            if name in Req:
                print(f"[OK] {name} ({version.strip()}) - {comment.strip()} ready")
            else:
                print(f"[ERROR] {name} ({version.strip()}) - {comment.strip()} is wrong")
    i = 0
    for i in range(len(Req) - 1):
        print(Req[i])
        if Req[i] not in data[0]:
            print("[MISSING]", name)
        else:
            i += 1
    # print("Analyzing Matrix data...")
    # print(f"Processing {1000} data points...")
    # print("Generating visualization...")

    # print("Analysis complete!")
    # print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
