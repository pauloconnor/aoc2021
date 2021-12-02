from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:


    depth=0
    distance=0
    lines = s.splitlines()
    for line in lines:
        instructions = line.split(" ")
        if instructions[0] == "up":
            depth = depth - int(instructions[1])
        elif instructions[0] == "down":
            depth = depth + int(instructions[1])
        else:
            distance = distance + int(instructions[1])

    print(distance*depth)
    return 0


INPUT_S = '''\

'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 1),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
