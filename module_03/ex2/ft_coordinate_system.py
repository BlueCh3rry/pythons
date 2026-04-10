import math


def get_player_pos() -> tuple:
    while True:
        user_input = input("Enter new coordinates as floats"
                           " in format 'x,y,z': ")
        try:
            parts = user_input.split(",")

            if len(parts) != 3:
                print("Invalid syntax")
                continue

            coords = []
            for part in parts:
                part = part.strip()
                try:
                    coords.append(float(part))
                except ValueError as e:
                    print(f"Error on parameter '{part}': {e}")
                    break
            else:
                return tuple(coords)
        except Exception:
            print("Invalid syntax")


def distance(p1: tuple, p2: tuple) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )


def main():
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    center = (0.0, 0.0, 0.0)
    dist_center = distance(center, pos1)
    print(f"Distance to center: {dist_center:.4f}")

    print("\nGet a second set of coordinates")
    pos2 = get_player_pos()
    dist_between = distance(pos1, pos2)
    print(f"Distance between the 2 sets of coordinates: {dist_between:.4f}")


if __name__ == "__main__":
    main()
