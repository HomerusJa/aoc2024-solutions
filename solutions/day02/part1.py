from itertools import pairwise
from pathlib import Path


def is_monotonic(levels: list[int]) -> bool:
    """Check if the levels are either strictly increasing or decreasing."""
    return sorted(levels) == levels or sorted(levels, reverse=True) == levels


def check_differences(levels: list[int], max_diff: int) -> bool:
    """Check...
    1. if the differences between the levels are less than or equal to the max_diff.
    2. if no two levels are equal.
    """
    return all(abs(a - b) <= max_diff and a != b for a, b in pairwise(levels))


def main() -> None:
    safe_reports: int = 0
    total_reports: int = 0

    with (Path(__file__).parent / "input.txt").open() as file:
        for line in file.readlines():
            levels = list(map(int, line.split(" ")))
            total_reports += 1

            if is_monotonic(levels) and check_differences(levels, 3):
                safe_reports += 1

    print(f"There are {safe_reports}/{total_reports} safe reports.")


if __name__ == "__main__":
    main()
