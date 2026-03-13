import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    id = input("Input Stream active. Enter archivist ID: ")
    rep = input("Input Stream active. Enter status report: ")
    sys.stdout.write(f"[STANDARD] Archive status from {id}: {rep}")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels verified")
    sys.stdout.write("[STANDARD] Data transmission complete")
    print("Three-channel communication test successful")


if __name__ == "__main__":
    main()
