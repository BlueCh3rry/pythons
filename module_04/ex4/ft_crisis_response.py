def main() -> None:
    print("=== CYBER ARCHIVES - RISIS RESPONSE SYSTEM ===\n")

    try:
        with open("ost_archive.txt", "w") as file:
            print(f"CRISIS ALERT: Attempting access to {file.name}...")
            print(f"SECURE EXTRACTION:\n{file.read()}")
    except (FileNotFoundError, PermissionError):
        print("RESPONSE: Archive not found in storage matrix")
    print("STATUS: Crisis handled, system stable")

    try:
        with open("classified_vault.txt", "w") as file:
            print(f"CRISIS ALERT: Attempting access to {file.name}...")
            file.close()
    except (FileNotFoundError, PermissionError):
        print("RESPONSE: Security protocols deny access")
    print("STATUS: Crisis handled, security maintained\n")

    try:
        with open("tandard_archive.txt", "w") as file:
            print(f"ROUTINE ACCESS: Attempting access to {file.name}...")
            print(f"SUCCESS: Archive recovered - ``{file.read()}''")
            file.close()
    except (FileNotFoundError, PermissionError):
        print("ERROR: File not found")
    print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
