# Python Standard Library
import argparse
import os
import sys

from collections import Counter

# pypi

# local modules

def get_input(file):
    with open(file, 'r') as f:
        data = f.readlines()
        data = [d.strip() for d in data]
        return data

if __name__ == "__main__":

    # Command line options
    # Create the parser
    my_parser = argparse.ArgumentParser(prog='Advent_of_Code', 
                    description='Solutions to Advent of Code problems.')

    # Add positional arguments
    my_parser.add_argument('year', type=int, help='Year 2015 to 2020', choices=range(2015, 2021))
    my_parser.add_argument('day', type=int, help='Day 1 through 25', choices=range(1, 26))
    my_parser.add_argument('part', type=int, help='Part 1 or 2', choices=range(1, 3))
    my_parser.add_argument('input_file', type=str, help='Path to input file')

    # Add optional arguments
    my_parser.add_argument('-v', '--verbose', action='store_true', help='an optional argument')

    # Execute the parse_args() method
    args = my_parser.parse_args()

    # Check if file exists
    path = os.path.join(os.getcwd(), args.input_file)
    if not os.path.isfile(path):
        print('The path specified does not exist: {}'.format(path))
        sys.exit()

    aoc_year = args.year
    aoc_day  = args.day
    aoc_part = args.part

    if aoc_year == 2015:
        from aoc_2015 import *
    elif aoc_year == 2016:
        from aoc_2016 import *
    elif aoc_year == 2017:
        from aoc_2017 import *
    elif aoc_year == 2018:
        from aoc_2018 import *
    elif aoc_year == 2019:
        from aoc_2019 import *
    elif aoc_year == 2020:
        from aoc_2020 import *

    # Solutions nested by day and part number
    solutions = {i: {1: f"Day: {i} Part 1", 2: f"Day: {i} Part 2"} for i in range(1, 26)}

    # Map functions to solutions
    solutions[1][1] = day_1
    solutions[1][2] = day_1
    solutions[2][1] = day_2
    solutions[2][2] = day_2
    solutions[3][1] = day_3
    solutions[3][2] = day_3
    solutions[4][1] = day_4
    solutions[4][2] = day_4
    solutions[5][1] = day_5
    solutions[5][2] = day_5
    solutions[6][1] = day_6
    solutions[6][2] = day_6
    solutions[7][1] = day_7
    solutions[7][2] = day_7
    solutions[8][1] = day_8
    solutions[8][2] = day_8
    solutions[9][1] = day_9
    solutions[9][2] = day_9
    solutions[10][1] = day_10
    solutions[10][2] = day_10
    solutions[11][1] = day_11
    solutions[11][2] = day_11
    solutions[12][1] = day_12
    solutions[12][2] = day_12
    solutions[13][1] = day_13
    solutions[13][2] = day_13
    solutions[14][1] = day_14
    solutions[14][2] = day_14
    solutions[15][1] = day_15
    solutions[15][2] = day_15
    solutions[16][1] = day_16
    solutions[16][2] = day_16
    solutions[17][1] = day_17
    solutions[17][2] = day_17
    solutions[18][1] = day_18
    solutions[18][2] = day_18
    solutions[19][1] = day_19
    solutions[19][2] = day_19
    solutions[20][1] = day_20
    solutions[20][2] = day_20
    solutions[21][1] = day_21
    solutions[21][2] = day_21
    solutions[22][1] = day_22
    solutions[22][2] = day_22
    solutions[23][1] = day_23
    solutions[23][2] = day_23
    solutions[24][1] = day_24
    solutions[24][2] = day_24
    solutions[25][1] = day_25
    solutions[25][2] = day_25

    # Print input
    if args.verbose:
        data = get_input(path)
        for d in enumerate(data):
            print(d)

    # Get data from input file
    data = get_input(path)

    # Execute solution
    sol = solutions[args.day][args.part]
    res = sol(args.part, data)
    print(f"Year: {aoc_year} Day: {aoc_day} Part: {aoc_part} Solution: {res}")

