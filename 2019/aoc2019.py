import argparse
import os
import sys
from intcode import Intcode

def get_input(file):
    with open(file, 'r') as f:
        data = f.readlines()
    data = [d.strip() for d in data]
    return data

def day_1(part, data):

    data = [int(num) for num in data]

    if part == 1:
        data = [num // 3 - 2 for num in data]
        return sum(data)
    elif part == 2:
        total = 0
        for mass in data:
            while mass > 0:
                fuel   = mass // 3 - 2
                total += max(0, fuel)
                mass   = fuel
        return total

def day_2(part, data):
    data = data[0].strip().split(',')

    if part == 1:
        program = Intcode(data)
        program.data[1] = 12
        program.data[2] = 2
        program.run(None)
        return program.data[0]   

    elif part == 2:
        for noun in range(len(data)):
            for verb in range(len(data)):
                program = Intcode(data)
                program.data[1] = noun
                program.data[2] = verb
                program.run(None)
                if int(program.data[0]) == 19690720:
                    return 100 * noun + verb

def day_3(part, data):
    directions = {'U': (-1,  0),
                  'D': ( 1,  0),
                  'L': ( 0, -1),
                  'R': ( 0,  1),}

    # Part 1

    """
    Each input has two rows of comma separated strings.
    <direction><number of steps> Example: R8 means go right 8 steps.
    """

    # Collect all cartesians coordinates (x, y) start from (0, 0)
    # given each instruction.
    all_paths = []
    for wire in data:
        wire  = wire.split(",")
        start = (0, 0)
        path  = []
        for inst in wire:
            d   = inst[0]
            num = int(inst[1:])
            while num > 0:
                x = start[0] + directions[d][0]
                y = start[1] + directions[d][1]
                start = (x, y)
                path.append(start)
                num -= 1
        all_paths.append(path)
    
    # Get the interesection of both wires.
    a = set(all_paths[0])
    b = set(all_paths[1])
    intersect = a.intersection(b)

    if part == 1:
        # Sort the intersection by Manhattan distance: abs(x) + abs(y)
        intersect = sorted(intersect, key= lambda x: abs(x[0]) + abs(x[1]))
        closest   = intersect[0]
        closest   = sum([abs(each) for each in closest])
    elif part == 2:
        wire1     = all_paths[0]
        wire2     = all_paths[1]
        intersect = sorted(intersect, key= lambda x: wire1.index(x) + wire2.index(x) + 2)
        closest   = intersect[0]
        closest   = wire1.index(closest) + wire2.index(closest) + 2      

    return closest

def day_4(part, data):
    pass

def day_5(part, data):
        pass
def day_6(part, data):
        pass
def day_7(part, data):
        pass
def day_8(part, data):
        pass
def day_9(part, data):
        pass
def day_10(part, data):
        pass
def day_11(part, data):
        pass
def day_12(part, data):
        pass
def day_13(part, data):
        pass
def day_14(part, data):
        pass
def day_15(part, data):
        pass
def day_16(part, data):
        pass
def day_17(part, data):
        pass
def day_18(part, data):
        pass
def day_19(part, data):
        pass
def day_20(part, data):
        pass
def day_21(part, data):
        pass
def day_22(part, data):
        pass
def day_23(part, data):
        pass
def day_24(part, data):
        pass
def day_25(part, data):
        pass

if __name__ == "__main__":

    # Command line options
    # Create the parser
    my_parser = argparse.ArgumentParser(prog='Advent_of_Code', 
                                        description='Solutions to Advent of Code problems.')

    # Add positional arguments
    my_parser.add_argument('day', type=int, help='Day 1 through 25', choices=range(1, 4))
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

    # Solutions nested by day and part number
    solutions = {i: {1: "Day: {} Part 1".format(i), 2: "Day: {} Part 2".format(i)} for i in range(1, 26)}

    # Map functions to solutions
    solutions[1][1] = day_1
    solutions[1][2] = day_1
    solutions[2][1] = day_2
    solutions[2][2] = day_2
    solutions[3][1] = day_3
    solutions[3][2] = day_3

    # Print input
    if args.verbose:
        data = get_input(path)
        for d in enumerate(data):
            print(d)

    # Get data from input file
    data = get_input(path)

    # Execute solution
    sol = solutions[args.day][args.part]
    print("Day {} Part {} Solution: {}".format(args.day, args.part, sol(args.part, data)))

