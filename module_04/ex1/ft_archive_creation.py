def main() -> None:
    print("=== CYBER ARCHIVES - RESERVATION SYSTEM ===\n")
    try:
        with open("new_discovery.txt", "w") as file:
            print(f"Initializing new storage unit: {file.name}")
            print("Storage unit created successfully..\n")
            print("Inscribing preservation data...")
            file.write("[ENTRY 001] New quantum algorithm discovered\n")
            file.write("[ENTRY 002] Efficiency increased by 347%\n")
            file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
            print("[ENTRY 001] New quantum algorithm discovered")
            print("[ENTRY 002] Efficiency increased by 347%")
            print("[ENTRY 003] Archived by Data Archivist trainee")
            file.close()
            print("\nData inscription complete. Storage unit sealed")
            print(f"Archive '{file.name}' ready for long-term preservation.")
    except IOError:
        print("ERROR: Storage unit not found")


if __name__ == "__main__":
    main()
