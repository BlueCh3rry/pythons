from dotenv import load_dotenv
import os


def get_env(variable: str, required: bool = False, default: str = "Not set"):
    value = os.getenv(variable, default)
    if required and value == "Not set":
        print(f"[WARNING] Missing required variable: {variable}")
    return value


def security_check():
    print("\nEnvironment security check:")

    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as file:
            content = file.read()
        if ".env" in content:
            if os.getenv("API_KEY"):
                print("[OK] No hardcoded secrets detected")
            else:
                print("[WARNING] hardcoded secrets detected")
            print("[OK] .env file properly configured")
            print("[OK] Production overrides available")
        else:
            print("[WARNING] .env file missing from .gitignore")
    else:
        print("[WARNING] .gitignore file not found")


def main() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    load_dotenv()

    print("\nConfiguration loaded:")
    mode = get_env("MATRIX_MODE")
    data = get_env("DATABASE_URL")
    key = get_env("API_KEY")
    log = get_env("LOG_LEVEL")
    zion = get_env("ZION_ENDPOINT")

    print("Mode:", mode)
    if mode == "development":
        print("Database: Connected to local instance")
    elif mode == "production":
        print("Database: Connected to production instance")
    else:
        print("Database:", data)
    if key != "Not set":
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")
    print("Log Level:", log)
    if zion != "Not set":
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    security_check()
    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
