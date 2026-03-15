import sys
import math


def check_char() -> tuple:
    list_dis = []
    for arg in sys.argv[1:]:
        parts = arg.split(",")
        for part in parts:
            try:
                list_dis.append(int(part))
            except ValueError as e:
                print("Parsing invalid coordinates:", arg)
                print("Error details - Type: ValueError, Args:", e)
                return 0
    if len(list_dis) != 3:
        print("Error: expected 3 coordinates")
        return 0
    print("Parsing coordinates: ", sys.argv[1:])
    print(f"Parsed position: ({list_dis[0]}, {list_dis[1]}, {list_dis[2]})")
    return tuple(list_dis)


def check_digit() -> tuple:
    list_dis = []
    for arg in sys.argv[1:]:
        try:
            list_dis.append(int(arg))
        except ValueError:
            return check_char()
    if len(list_dis) != 3:
        print("Error: expected 3 coordinates")
        return 0
    print(f"Position created: ({list_dis[0]}, {list_dis[1]}, {list_dis[2]})")
    return tuple(list_dis)


def check_position() -> tuple:
    for arg in sys.argv[1:]:
        if "," in arg:
            return check_char()
    return check_digit()


def main() -> str:
    print("=== Game Coordinate System ===\n")
    if len(sys.argv) == 1:
        return "No coordinates provided"
    tuple_dis = check_position()
    if tuple_dis == 0:
        return "No coordinates"
    x2 = int(tuple_dis[0])
    y2 = int(tuple_dis[1])
    z2 = int(tuple_dis[2])
    tuple_pos = (0, 0, 0)
    x1 = int(tuple_pos[0])
    y1 = int(tuple_pos[1])
    z1 = int(tuple_pos[2])
    res = "%.2f" % math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}): {res}")

    # print("Unpacking demonstration:")
    # print(f"Parsed position: , ({x1}, {y1}, {z1})")
    # print(f"Coordinates:", {X}, {Y}, {Z}")


if __name__ == "__main__":
    main()
