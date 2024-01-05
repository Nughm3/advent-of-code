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

## Fish shell script

In 2023 I switched to using this function with the Fish shell:

```fish
function aoc
    set day (date +%-d)
    set year (date +%Y)

    set input_file "input$day"
    set solution_file "day$day.py"

    if not test -e $input_file
        curl -s -b session=$AOC_SESSION_ID "https://adventofcode.com/$year/day/$day/input" -o $input_file
    end

    if not test -e $solution_file
        echo -e "\
with open(\"$input_file\") as f:
    data = f.read().splitlines()\n\n" > $solution_file
    end

    if test $EDITOR = "hx" -o $EDITOR = "helix"
        $EDITOR $solution_file:(count < $solution_file)
    else if test $EDITOR = "vim" -o $EDITOR = "nvim"
        $EDITOR $solution_file +
    else
        $EDITOR $solution_file
    end
end
```
