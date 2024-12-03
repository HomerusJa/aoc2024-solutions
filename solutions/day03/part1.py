import re
from pathlib import Path

# MUL_REGEX = re.compile(r"mul\(\d+,\d+\)")
MUL_REGEX = re.compile(r"mul\((\d+),(\d+)\)")


def extract_and_multiply(text: str) -> int:
    total_sum = 0
    for match in MUL_REGEX.finditer(text):
        a, b = map(int, match.groups())
        total_sum += a * b
    return total_sum

def main() -> None:
    with open(Path(__file__).parent / "input.txt") as file:
        total_sum = extract_and_multiply(file.read())
        print(total_sum)


if __name__ == "__main__":
    main()
