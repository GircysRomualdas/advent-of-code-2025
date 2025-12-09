import os
import re

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
INPUT_DIR = os.path.join(PROJECT_ROOT, "input")
TEST_DATA_PATH = os.path.join(INPUT_DIR, "test.txt")
INPUT_DATA_PATH = os.path.join(INPUT_DIR, "input.txt")


def read_data(path: str) -> str:
    with open(path, "r") as f:
        data = f.read()
    return data


def main():
    # data = read_data(TEST_DATA_PATH)
    data = read_data(INPUT_DATA_PATH)

    id_ranges = data.strip().split(",")

    result = []
    for id_str in id_ranges:
        ids = id_str.split("-")
        id_from = int(ids[0])
        id_to = int(ids[1])

        sub_result = []
        for id in range(id_from, id_to + 1):
            id_s = str(id)

            match = re.search(r"^(\d+)\1+$", id_s)

            if match:
                sub_result.append(int(match.group(0)))

        if sub_result:
            print(f"{id_str} has invalid IDs: {sub_result}")
            result.extend(sub_result)

    print(f"Adding up all the invalid IDs in this example produces {sum(result)}")


if __name__ == "__main__":
    main()
