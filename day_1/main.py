import os


def read_data(path: str) -> list[str]:
    with open(path, "r") as f:
        data = f.read().splitlines()
    return data


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(PROJECT_ROOT, "input")
TEST_DATA_PATH = os.path.join(INPUT_DIR, "test.txt")
INPUT_DATA_PATH = os.path.join(INPUT_DIR, "input.txt")


def main():
    # data = read_data(TEST_DATA_PATH)
    data = read_data(INPUT_DATA_PATH)

    pointing = 50
    count_0 = 0
    print(f"The dial starts by pointing at {pointing}")
    for item in data:
        rotation = item[0]
        distance = int(item[1:])

        if rotation == "L":
            pointing = (pointing - distance) % 100
        elif rotation == "R":
            pointing = (pointing + distance) % 100

        if pointing == 0:
            count_0 += 1

        print(f"The dial is rotated {item} to point at {pointing}")

    print(f"Number of times the dial points at 0: {count_0}, password: {count_0}")


if __name__ == "__main__":
    main()
