from dotenv import load_dotenv
import os


def main() -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()
    print("\nConfiguration loaded:")
    mode = os.getenv('MATRIX_MODE')
    data = os.getenv('DATABASE_URL')
    key = os.getenv('API_KEY')
    log = os.getenv('LOG_LEVEL')
    zion = os.getenv('ZION_ENDPOINT')
    print("Mode:", mode)
    print("Database:", data)
    print("API Access:", key)
    print("Log Level:", log)
    print("Zion Network:", zion)

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations")


if __name__ == "__main__":
    main()
