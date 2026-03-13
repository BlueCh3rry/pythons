def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")

    try:
        with open("classified_data.txt", "w") as file:
            print()
            print(f"SECURE EXTRACTION:\n{file.read()}")
    except IOError:
        print("ERROR: Storage unit not found")

    try:
        with open("security_protocols.txt", "w") as file:
            print()
            print(f"SECURE PRESERVATION:\n{file.read()}")
            file.close()
            print("Vault automatically sealed upon completion")
    except IOError:
        print("ERROR: Storage unit not found")
    print("All vault operations completed with maximum security")


if __name__ == "__main__":
    main()
