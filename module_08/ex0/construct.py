import sys
import os
import site


def main() -> None:
    inside_venv = sys.prefix != sys.base_prefix
    venv_name = os.path.basename(sys.prefix)
    print()
    if not inside_venv:
        print("MATRIX STATUS: You're still plugged in")
        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again")
    else:
        site_packages = site.getsitepackages()[0]
        print("MATRIX STATUS: Welcome to the construct")
        print("\nCurrent Python:", sys.executable)
        print("Virtual Environment:", venv_name)
        print("Environment Path:", sys.prefix)
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("\nPackage installation path:")
        print(site_packages)


if __name__ == "__main__":
    main()
