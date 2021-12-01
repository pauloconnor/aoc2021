from __future__ import annotations

import argparse
import os.path

import pytest

from support import timing

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    numbers = [int(line) for line in s.splitlines()]
    for n in numbers:
        pass

    lines = s.splitlines()
    for line in lines:
        pass

    last_numbers = []
    last = 0
    increased = -1
    for n in numbers:
        if len(last_numbers) < 3:
            last_numbers.append(n)
        else:
            last_numbers.pop(0)
            last_numbers.append(n)
            count = last_numbers[0] + last_numbers[1] + last_numbers[2]
            if count > last:
                increased = increased + 1
                print("%s (increased)" % count)
            last = count
            
        
    print(increased)
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
