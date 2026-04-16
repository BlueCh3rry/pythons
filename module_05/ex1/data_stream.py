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

        return self.counter, value


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if isinstance(data, list):
            for x in data:
                self.storage.append(str(x))
                self.counter += 1
        else:
            self.storage.append(str(data))
            self.counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list) and data:
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: Any) -> None:
        if isinstance(data, list):
            for x in data:
                self.storage.append(x)
                self.counter += 1
        else:
            self.storage.append(data)
            self.counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_valid_dict(d):
            return (isinstance(d, dict) and 
                    "log_level" in d and "log_message" in d)

        if is_valid_dict(data):
            return True
        if isinstance(data, list) and data:
            return all(is_valid_dict(item) for item in data)
        return False

    def ingest(self, data: Any) -> None:
        def format_log(d: dict) -> str:
            return f"{d.get('log_level')}: {d.get('log_message')}"

        if isinstance(data, list):
            for item in data:
                self.storage.append(format_log(item))
                self.counter += 1
        else:
            self.storage.append(format_log(data))
            self.counter += 1


class DataStream():
    def __init__(self):
        self.processors = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for item in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(item):
                    proc.ingest(item)
                    handled = True
                    break
            if not handled:
                print("DataStream error - Can't process element in stream:",
                      f"{item}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}: total {proc.counter} items processed, "
                  f"remaining {len(proc.storage)} on processor")


def main():
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Numeric Processor")
    np = NumericProcessor()
    ds.register_processor(np)

    stream = ['Hello world', [3.14, -1, 2.71],
              [{'log_level': 'WARNING', 'log_message':
                'Telnet access! Use ssh instead'},
               {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
              42, ['Hi', 'five']]

    print(f"\nSend first batch of data on stream: {stream}")
    ds.process_stream(stream)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    tp = TextProcessor()
    lp = LogProcessor()
    ds.register_processor(tp)
    ds.register_processor(lp)

    print("Send the same batch again")
    ds.process_stream(stream)
    ds.print_processors_stats()

    print("\nConsume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")

    for _ in range(3):
        np.output()
    for _ in range(2):
        tp.output()
    for _ in range(1):
        lp.output()

    ds.print_processors_stats()


if __name__ == "__main__":
    main()