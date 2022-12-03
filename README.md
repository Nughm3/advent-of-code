# advent-of-code

Solutions to Advent of Code.

[Advent of Code](https://adventofcode.com) is a yearly programming competition hosted from December 1-25.

## Advent of Code helper

`aoc.py` is a helper Python script for solving AoC problems.

It can open today's puzzle:

```bash
./aoc.py
```

Import it as a library to let it fetch inputs for you.

```python
import aoc

input = aoc.input()

yesterday = aoc.day - 1
assert yesterday > 0
yesterday_input = aoc.input(day=yesterday)
```

If you prefer to just read a file manually, just use `read_file`:

```python
from aoc import read_file

input = read_file("input")
```