import re
from pathlib import Path


def main() -> None:
    with open(Path(__file__).parent / "input.txt") as file:
        enabled: bool = True
        total_sum: int = 0

        # Match any of the following:
        # - mul(a, b)
        # - do()
        # - don't()
        for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", file.read()):
            instruction = match.group()
            if instruction == "do()":
                enabled = True
            elif instruction == "don't()":
                enabled = False
            # elif instruction.startswith("mul("):
            else:
                if enabled:
                    a, b = map(int, match.groups())
                    total_sum += a * b

    print(total_sum)

if __name__ == "__main__":
    main()
