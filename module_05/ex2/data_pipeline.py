from abc import ABC, abstractmethod
from typing import Any, Protocol
import json


class DataProcessor(ABC):
    def __init__(self):
        self.storage = []
        self.counter = 0
        self.output_index = -1

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
        self.output_index += 1
        return self.output_index, value


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


def is_valid_dict(d):
    return (isinstance(d, dict) and "log_level" in d and "log_message" in d)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
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


class CSVExportPlugin:
    def __init__(self):
        pass

    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        print(",".join(values))


class JSONExportPlugin:
    def __init__(self):
        pass

    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = {}

        for idx, (counter, value) in enumerate(data):
            key = f"item_{counter}"
            result[key] = value

        print("JSON Output:")
        print(json.dumps(result))


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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
            if not handled:
                print("DataStream error - Can't process element "
                      "in stream:", item)

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(f"{name}: total {proc.counter} items processed, "
                  f"remaining {len(proc.storage)} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            extracted = []
            for _ in range(nb):
                if not proc.storage:
                    break
                extracted.append(proc.output())
            if extracted:
                plugin.process_output(extracted)


def main():
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("\nRegistering Processors")
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)

    stream = ['Hello world',
              [3.14, -1, 2.71],
              [{'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'},
               {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
              42,
              ['Hi', 'five']]

    print(f"\nSend first batch of data on stream: {stream}")
    ds.process_stream(stream)
    ds.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, CSVExportPlugin())
    ds.print_processors_stats()

    stream2 = [21,
               ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
               [{'log_level': 'ERROR',
                 'log_message': '500 server crash'},
                {'log_level': 'NOTICE',
                 'log_message': 'Certificate expires in 10 days'}],
               [32, 42, 64, 84, 128, 168],
               'World hello']

    print(f"\nSend another batch of data: {stream2}")
    ds.process_stream(stream2)
    ds.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, JSONExportPlugin())
    ds.print_processors_stats()


if __name__ == "__main__":
    main()
