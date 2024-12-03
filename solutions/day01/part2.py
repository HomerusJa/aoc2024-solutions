from collections import Counter
from pathlib import Path


def read_input() -> tuple[list[int], list[int]]:
    """Reads the input file and returns the values."""
    left_values: list[int] = []
    right_values: list[int] = []

    with (Path(__file__).parent / "input.txt").open("r") as file:
        for line in file.readlines():
            left, right = map(int, line.split())
            left_values.append(left)
            right_values.append(right)

    return left_values, right_values


def main() -> None:
    similarity_score: int = 0

    print("Reading the input file...")
    left_values, right_values = read_input()

    print("Filtering the duplicates in the left list...")
    left_values = list(set(left_values))

    print("Counting the values in the right list...")
    counts = Counter(right_values)

    print("Calculating the similarity score...")
    for num in left_values:
        similarity_score += counts[num] * num

    print(f"The similarity score is {similarity_score}.")


if __name__ == "__main__":
    main()
