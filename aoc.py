#!/usr/bin/env python3

# aoc.py: helper for Advent of Code.
# Import aoc.py as a library to use the utility functions.
# IMPORTANT: make sure to set the AOC_SESSION environment variable.

from datetime import datetime

today = datetime.today()
day = today.day
year = today.year

# Simple helper to read a file
def read_file(path=f"{day}.in"):
    with open(path) as f:
        return f.read()

# Get puzzle input for today's puzzle
def today(cache=True):
    return input(day, year)

# Get puzzle input for an event
def input(day, year, cache=True):
    import requests, os
    assert day >= 1 and day <= 25

    path = f"{day}.in"
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = os.environ["AOC_SESSION"]

    if os.path.isfile(path):
        print(f"aoc: Using cached input '{path}'")
        return read_file(path)

    print("aoc: Downloading input...")

    req = requests.get(
        input_url,
        cookies={"session": session},
        headers={"user-agent": "https://github.com/Nughm3/advent-of-code"},
    )

    if req.status_code == 404:
        raise Exception("Puzzle input not available yet!")

    input = req.text

    if cache:
        with open(path, "w") as f:
            f.write(input)
        print(f"aoc: Input cached to '{path}'")

    return input


# Benchmark a function
def bench(func):
    import time
    from functools import wraps

    @wraps(func)
    def bench_wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        duration = time.perf_counter() - start
        print(f"bench: '{func.__name__}' finished in {duration:.3f}s")

    return bench_wrapper

if __name__ == "__main__":
    print("Import `aoc` to use it as a utility for fetching puzzle inputs.")
    
    api = {
        "input(DAY, YEAR)": "get puzzle input for day DAY in event YEAR",
        "today()": "get today's puzzle input, recommended to switch to input() later as this changes every day",
        "read_file(PATH?)": "read the file at PATH, defaults to today's input DAY.in",
        "@bench": "decorator to time a function and print its runtime"
    }
    
    for k, v in api.items():
        print(f" - aoc.{k}: {v}")
    
    print("Make sure the AOC_SESSION environment variable is set to your session cookie.")
