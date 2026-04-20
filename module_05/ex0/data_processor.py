from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self.storage = []
        self.counter = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.storage:
            raise Exception("No data to output")
        value = self.storage.pop(0)
        rank = self.counter
        self.counter += 1
        return rank, value


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for x in data:
                self.storage.append(str(x))
        else:
            self.storage.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            self.storage.extend(data)
        else:
            self.storage.append(data)


def is_valid_dict(d: Any) -> bool:
    return (
        isinstance(d, dict)
        and "log_level" in d
        and "log_message" in d
        and isinstance(d["log_level"], str)
        and isinstance(d["log_message"], str)
    )


def format_log(d: dict) -> str:
    return f"{d.get('log_level')}: {d.get('log_message')}"


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(item) for item in data)
        return False

    def ingest(self, data: Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                self.storage.append(format_log(item))
        else:
            self.storage.append(format_log(data))


def handle_num():
    np = NumericProcessor()
    print(" Trying to validate input '42':", np.validate(42))
    print(" Trying to validate input 'Hello':", np.validate("Hello"))
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")
    except Exception as e:
        print(" Got exception:", e)
    print(" Processing data: [1, 2, 3, 4, 5]")
    np.ingest([1, 2, 3, 4, 5])

    print(" Extracting 3 values...")
    for _ in range(3):
        rank, value = np.output()
        print(f" Numeric value {rank}: {value}")


def handle_text():
    tp = TextProcessor()
    print(" Trying to validate input '42':", tp.validate(42))
    print(" Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(["Hello", "Nexus", "World"])

    print(" Extracting 1 value...")
    rank, value = tp.output()
    print(f" Text value {rank}: {value}")


def handle_log():
    lp = LogProcessor()
    print(" Trying to validate input 'Hello':", lp.validate("Hello"))
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},]
    print(" Processing data:", logs)
    lp.ingest(logs)

    print(" Extracting 2 values...")
    for _ in range(2):
        rank, value = lp.output()
        print(f" Log entry {rank}: {value}")


def main():
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    handle_num()

    print("\nTesting Text Processor...")
    handle_text()

    print("\nTesting Log Processor...")
    handle_log()


if __name__ == "__main__":
    main()
