def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        with open("ancient_fragment.txt", "r") as file:
            print(f"Accessing Storage Vault: {file.name}")
            print("Connection established...\n")
            print(f"RECOVERED DATA:\n{file.read()}")
            file.close()
            print("\nData recovery complete. Storage unit disconnected")
    except IOError:
        print("ERROR: Storage vault not found")


if __name__ == "__main__":
    main()
