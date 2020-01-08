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

`aoc2019.py` - Solutions to Advent of Code 2019.

`test_aoc2019.py` - Unit tests based on AOC instructions and solved problems.

`2019\input` - Input files from AOC.

## Sample Usage 

```console
$python aoc2019.py 1 1 01_input.txt

Day 1 Part 1 Solution: 3391707
```

```console
$python aoc2019.py <day #> <part #> <input_file>
```