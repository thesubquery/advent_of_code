# Advent of Code
Python command line tool for solutions to Advent of Code.

## Folder structure
```
advent_of_code
│   .gitignore
│   LICENSE
│   README.md
│
└───2019
    │   aoc2019.py
    │   test_aoc2019.py
    │
    ├───input
    │       day_1.txt
    │       day_2.txt
    │       ...
```

`aoc*.py` - Solutions to Advent of Code for that year.

`test_aoc*.py` - Unit tests based on AOC instructions and solved problems.

`*\input` - Input files from AOC.

`*\writeups` - Write ups for each day.

## Usage 

**Format**
```shell
$python aoc2019.py <day #> <part #> <input_file>
```

**Sample Usage**
```shell
$python aoc2019.py 1 1 day_1.txt
Day 1 Part 1 Solution: 3391707
```
