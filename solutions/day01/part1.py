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
    sum_of_differences: int = 0

    print("Reading the input file...")
    left_values, right_values = read_input()

    print("Sorting the values...")
    left_values.sort()
    right_values.sort()

    print("Calculating the sum of differences...")
    for left, right in zip(left_values, right_values, strict=False):
        # We need to use abs() because the difference can be negative.
        sum_of_differences += abs(left - right)

    print(f"The sum of differences is {sum_of_differences}.")


if __name__ == "__main__":
    main()
