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

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
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

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")

        if isinstance(data, list):
            self.storage.extend(data)
        else:
            self.storage.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_dict(d):
            return (
                isinstance(d, dict)
                and all(isinstance(k, str) and isinstance(v, str) for k, v in d.items())
            )

        if is_valid_dict(data):
            return True
        if isinstance(data, list):
            return all(is_valid_dict(item) for item in data)
        return False

    def ingest(self, data: dict[str, str]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")

        def format_log(d: dict[str, str]) -> str:
            level = d.get("log_level", "")
            message = d.get("log_message", "")
            return f"{level}: {message}"

        if isinstance(data, list):
            for item in data:
                self.storage.append(format_log(item))
        else:
            self.storage.append(format_log(data))


class DataStream():
    def register_processor(self, proc: DataProcessor) -> None:
        pass

    def process_stream(self, stream: list[Any]) -> None:
        pass

    def print_processors_stats(self) -> None:
        pass


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
    print("=== Code Nexus - Data Steam ===\n")
    print("Testing Numeric Processor...")
    handle_num()

    print("\nTesting Text Processor...")
    handle_text()

    print("\nTesting Log Processor...")
    handle_log()


if __name__ == "__main__":
    main()
