#!/usr/bin/env python3

# aoc.py: helper for Advent of Code.
# https://adventofcode.com

# Run as a command-line program to open today's problem.
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


# Get puzzle input as a string. Will cache it if it is downloaded.
def input(day=day, cache=True):
    import requests, os

    path = f"{day}.in"
    input_url = f"https://adventofcode.com/{year}/day/{day}/input"

    if os.path.isfile(path):
        print(f"aoc: Using cached input '{path}'")
        return read_file(path)

    print("aoc: Downloading input...")
    session = os.environ["AOC_SESSION"]
    req = requests.get(input_url, cookies={"session": session})

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
    if today.month != 12 or day > 25:
        print("Advent of Code is not currently running!")
    else:
        url = f"https://adventofcode.com/{year}/day/{day}"

        print(f"Advent of Code {year} (day {day})\n{url}")
        print("\nOpening in web browser...")

        import webbrowser

        webbrowser.open(url)
