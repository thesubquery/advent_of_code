import argparse
import os
import sys

class Intcode():
    def __init__(self, data):
        
        self.data        = [each for each in data]

        self.ptr         = 0
        self.opcode_args = {1: 3,
                            2: 3,
                            3: 1,
                            4: 1,
                            5: 2,
                            6: 2,
                            7: 3,
                            8: 3,
                            99: 0}

    def __repr__(self):
        result = [self.opcode] + self.param_mode
        return "|".join([str(each) for each in result])
    
    def get_arg(self, mode, arg, data):
        if mode == 0:
            return int(data[arg])
        elif mode == 1:
            return arg

    def get_num_args(self):
        return self.opcode_args[self.opcode]

    def update_inst(self):
        opcode          = self.data[self.ptr]
        self.opcode     = int(opcode[-2:])
        self.param_mode = [0, 0, 0]
        if len(opcode) > 2:
            index = 0
            for each in opcode[-3:-6:-1]:
                self.param_mode[index] = int(each)
                index += 1        
            
    def run(self, ID):
        self.ID = ID
        self.update_inst()
        while self.opcode != 99:
            
            num   = self.get_num_args()
            args  = [int(each) for each in self.data[self.ptr+1:self.ptr+1+num]]
            
            print(self.ptr, self.opcode, args, self.data[self.ptr:self.ptr+num+1])
            
            if self.opcode == 1:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                self.data[args[2]] = str(val1 + val2)
            elif self.opcode == 2:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                self.data[args[2]] = str(val1 * val2)
            elif self.opcode == 3:
                self.data[args[0]] = str(self.ID)
            elif self.opcode == 4:
                self.ID = int(self.data[args[0]])
            elif self.opcode == 5:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 > 0:
                    self.ptr = val2
                    self.update_inst()
                    continue
            elif self.opcode == 6:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 == 0:
                    self.ptr = val2
                    self.update_inst()
                    continue
            elif self.opcode == 7:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 < val2:
                    self.data[args[2]] = '1'
                else:
                    self.data[args[2]] = '0'
            elif self.opcode == 8:
                val1          = self.get_arg(self.param_mode[0], args[0], self.data)
                val2          = self.get_arg(self.param_mode[1], args[1], self.data)
                if val1 == val2:
                    self.data[args[2]] = '1'
                else:
                    self.data[args[2]] = '0'
            self.ptr += num + 1
            self.update_inst()


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


if __name__ == "__main__":

    # Command line options
    # Create the parser
    my_parser = argparse.ArgumentParser(prog='Advent_of_Code', 
                                        description='Solutions to Advent of Code problems.')

    # Add positional arguments
    my_parser.add_argument('day', type=int, help='Day 1 through 25', choices=range(1, 2))
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

    data = get_input(path)

    # Execute solution
    sol = solutions[args.day][args.part]
    print("Day {} Part {} Solution: {}".format(args.day, args.part, sol(args.part, data)))
    

    # print(vars(args))
    # print(solutions[args.day][args.part])

    # print(path)


