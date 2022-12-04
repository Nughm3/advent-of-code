# advent-of-code

Solutions to Advent of Code.

[Advent of Code](https://adventofcode.com) is a yearly programming competition hosted from December 1-25.

## Advent of Code helper

`aoc.py` is a helper Python script for solving AoC problems. Import it as a library to let it fetch inputs for you.

```python
import aoc

today = aoc.today()
yesterday = aoc.input(aoc.day - 1, aoc.year)
```

If you prefer to just read a file manually, just use `read_file`:

```python
from aoc import read_file
input = read_file("input")
```