import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(PROJECT_ROOT, "input")
TEST_DATA_PATH = os.path.join(INPUT_DIR, "test.txt")
INPUT_DATA_PATH = os.path.join(INPUT_DIR, "input.txt")


def read_data(path: str) -> list[str]:
    with open(path, "r") as f:
        data = f.read().splitlines()
    return data


def crossings(start, distance, direction):
    count = 0
    for i in range(1, distance + 1):
        pos = 0
        if direction == "R":
            pos = (start + i) % 100
        elif "L":
            pos = (start - i) % 100

        if pos == 0:
            count += 1
    return count


def main():
    # data = read_data(TEST_DATA_PATH)
    data = read_data(INPUT_DATA_PATH)

    pointing = 50
    count_0 = 0
    print(f"The dial starts by pointing at {pointing}")
    for item in data:
        rotation = item[0]
        distance = int(item[1:])

        time_pointed_to_0 = crossings(pointing, distance, rotation)

        if rotation == "R":
            pointing = (pointing + distance) % 100
        elif "L":
            pointing = (pointing - distance) % 100

        count_0 += time_pointed_to_0

        msg = f"The dial is rotated {item} to point at {pointing}"
        if time_pointed_to_0 != 0 and pointing != 0:
            msg += f"; during this rotation, it points at 0 {time_pointed_to_0} time{'s' if time_pointed_to_0 > 1 else ''}."
        print(msg)

    print(f"Number of times the dial points at 0: {count_0}, password: {count_0}")


if __name__ == "__main__":
    main()
