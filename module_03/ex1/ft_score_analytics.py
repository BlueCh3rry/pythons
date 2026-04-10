import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print("No scores provided.",
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    array = []
    for arg in sys.argv[1:]:
        try:
            array.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if array:
        print("Total players:", len(array))
        print("Total score:", sum(array))
        print("Average score:", sum(array) / len(array))
        print("High score:", max(array))
        print("Low score:", min(array))
        print("Score range:", max(array) - min(array))
        print()
    else:
        print("No scores provided.",
              "Usage: python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
