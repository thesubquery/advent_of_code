# Advent of Code
Python command line tool for solutions to Advent of Code.

## Manifest
```
├── LICENSE
├── README.md
├── __pycache__
│   └── aoc_2015.cpython-38.pyc
├── advent_of_code.code-workspace
├── aoc.py
├── aoc_2015.py
├── aoc_2019.py
├── aoc_2020.py
├── data
│   ├── 2015
│   │   └── day_1.txt
│   ├── 2016
│   ├── 2017
│   ├── 2018
│   ├── 2019
│   │   ├── day_1.txt
│   │   ├── day_2.txt
│   │   ├── day_3.txt
│   │   ├── day_4.txt
│   │   ├── day_5.txt
│   │   └── day_6.txt
│   └── 2020
│       ├── day_1.txt
│       └── day_2.txt
├── intcode.py
└── test
    ├── test_aoc2015.py
    ├── test_aoc2019.py
    └── test_aoc2020.py
```

`aoc.py` - Main program to get all solutions.

`aoc_*.py` - Solutions to Advent of Code for that year.

`test_aoc*.py` - Unit tests based on AOC instructions and solved problems.

`data/<year>` - Input files from AOC.

## Usage 

**Format**
```shell
$python aoc.py <year> <day> <part> <input_file>
```

**Sample Usage**
```shell
$python aoc.py 2015 1 1 data/2015/day_1.txt
Year: 2015 Day: 1 Part: 1 Solution: 232
```
