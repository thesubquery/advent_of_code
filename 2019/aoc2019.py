import argparse
import os
import sys

def get_input(file):
    with open(file, 'r') as f:
        data = f.readlines()
    data = [d.strip() for d in data]
    return data

def day_1(part, file):
    data = get_input(file)
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


if __name__ == "__main__":


    # Command line options
    # Create the parser
    my_parser = argparse.ArgumentParser(prog='Advent_of_Code', 
                                        description='Solutions to Advent of Code problems.')

    # Add positional arguments
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

    # Solutions nested by day and part number
    solutions = {i: {1: "Day: {} Part 1".format(i), 2: "Day: {} Part 2".format(i)} for i in range(1, 26)}

    solutions[1][1] = day_1
    solutions[1][2] = day_1

    # Print input
    if args.verbose:
        data = get_input(path)
        for d in enumerate(data):
            print(d)


    # Execute solution
    sol = solutions[args.day][args.part]
    print("Solution: {}".format(sol(args.part, path)))
    

    # print(vars(args))
    # print(solutions[args.day][args.part])

    # print(path)


