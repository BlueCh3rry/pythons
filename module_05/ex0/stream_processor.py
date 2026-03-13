from abc import ABC, abstractmethod

class DataProcessor(ABC):
    def __init__(self,  data: Any):
        self.data = data

    @abstractmethod
    def process(self, data: Any) -> str:
        pass
    def validate(self, data: Any) -> bool:
        return 0

class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return 0

    def validate(self, data: Any) -> bool:
        return 0

    def format_output(self, result: str) -> str:
        return 0

class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return 0

    def validate(self, data: Any) -> bool:
        return 0

    def format_output(self, result: str) -> str:
        return 0

class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return 0

    def validate(self, data: Any) -> bool:
        return 0

    def format_output(self, result: str) -> str:
        return 0


def handle_digit(arr):
    print(f"Processing data: {arr}")
    for elem in arr:
        try:
            int(elem)
        except ValueError:
            return 0
    print("Validation: Numeric data verified")
    sum = 0
    number_count = 0
    for number in arr:
        number_count += 1
        sum = sum + elem
    avg = sum/number_count
    print(f"Output: Processed {number_count} numeric values, sum={sum}, avg={avg}")


def handle_str(str):
    print(f"Processing data: {str}")
    for elem in str:
        try:
            isinstance(elem, str)
        except ValueError:
            return 0
    print("Validation: Text data verified")
    for char in str:
        if char != ' ':
            char_count += 1
        else:
            words += 1
    print(f"Output: Processed text: {char} characters, {words} words")


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("Initializing Numeric Processor...")
    lst = [1, 2, 3, 4, 5]
    handle_digit(lst)
    print()
    print("Initializing Text Processor...")
    str = "Hello Nexus World"
    handle_str(str)
    print()
    print("Initializing Log Processor...")


Processing data: "ERROR: Connection timeout"
Validation: Log entry verified
Output: [ALERT] ERROR level detected: Connection timeout


if __name__ == "__main__":
    main()
