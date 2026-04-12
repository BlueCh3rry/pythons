import random
from typing import Any, Generator, Tuple


def gen_event() -> Generator[Tuple[Any, Any], None, None]:
    act = ["eat", "sleep", "move", "swim", "climb", "release", "run", "use"]
    players = ["alice", "bob", "charlie", "dylan"]
    while True:
        action = random.choice(act)
        player = random.choice(players)
        yield (player, action)


def consume_event(lst: list) -> Generator[Any, None, None]:
    while lst:
        events = random.choice(lst)
        print(f"Got event from list: {events}")
        lst.remove(events)
        yield lst


def main():
    print("=== Game Data Stream Processor ===")

    gen = gen_event()
    for i in range(1000):
        player, action = next(gen)
        print(f"Event {i}: Player {player} did action {action}")

    lst = []
    for i in range(10):
        event = next(gen)
        lst.append(event)
    print(f"Built list of 10 events: {lst}")
    for event in consume_event(lst):
        print("Remains in list:", lst)


if __name__ == "__main__":
    main()
