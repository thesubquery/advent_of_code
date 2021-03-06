# Python Standard Library
import argparse
import os
import re
import sys

from collections import Counter, defaultdict, deque

# pypi

# Common

def get_input(file):
    with open(file, 'r') as f:
        data = f.readlines()
    data = [d.strip() for d in data]
    return data

def day_1(part, data):

    data = [int(num) for num in data]

    if part == 1:
        visited = set()
        for num in data:
            comp = 2020 - num
            if comp in visited:
                return num * comp
            else:
                visited.add(num)

    elif part == 2:

        # 3Sum Problem
        
        N = len(data)
        data.sort()
        comps = set(data)

        for i in range(N-2):
            for j in range(i+1, N-1):
                comp = 2020 - data[i] - data[j]
                if comp in comps:
                    return data[i] * data[j] * comp
                elif comp < data[j]:
                    break

def day_2(part, data):

    pattern = "(\d+)-(\d+) ([a-z]{1}): ([a-z]+)"
    prog = re.compile(pattern)

    valid = 0

    for string in data:
        inst = prog.match(string.strip())
        if not inst:
            raise Exception(f"Pattern '{pattern}' did not find a match in string '{string}'.")
        else:
            inst = inst.groups()

        lower = int(inst[0])
        upper = int(inst[1])
        ltr   = inst[2]
        pw    = inst[3]

        if part == 1:
            pw = Counter(pw)
            if ltr in pw:
                if lower <= pw[ltr] <= upper:
                    valid += 1

        elif part == 2:
            if upper <= len(pw):
                if ltr in [pw[lower-1], pw[upper-1]] and pw[lower-1] != pw[upper-1]:
                    valid += 1
    
    return valid

def day_3(part, data):
        
    def explore(right: int, down: int, forest: list):
        x = 0
        y = 0
        y_length = len(forest[0].strip())
        res = defaultdict(int)
        while x < len(forest):
            val = forest[x][y % y_length]
            res[val] += 1
            x += down
            y += right
        return res['#']
    
    if part == 1:        
        return explore(3, 1, data)
    elif part == 2:
        slopes = [(1, 1),
                  (3, 1),
                  (5, 1),
                  (7, 1),
                  (1, 2)]
        
        res = 1
        for slope in slopes:
            res *= explore(slope[0], slope[1], data)
        return res
        
def day_4(part, data):

    class Passport:
        def __init__(self):
            self.data = {
                'byr': None,
                'iyr': None,
                'eyr': None,
                'hgt': None,
                'hcl': None,
                'ecl': None,
                'pid': None,
                'cid': None
            }
        def add_attr(self, key, value):
            if key not in self.data:
                print(key)
            if self.data[key]:
                print(key, self.data[key])
            self.data[key] = value

        def is_valid(self, part):
            if part == 1:
                valid_attr = [key for key in self.data.keys() if self.data[key] and key != 'cid']
                return len(valid_attr) == 7
            elif part == 2:
                p = self.data
                # byr (Birth Year) - four digits; at least 1920 and at most 2002.
                if not (p['byr'] and re.match('^[0-9]{4}$', p['byr']) and 1920 <= int(p['byr']) <= 2002):
                    return False
                # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                if not (p['iyr'] and re.match('^[0-9]{4}$', p['iyr']) and 2010 <= int(p['iyr']) <= 2020):
                    return False
                # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                if not (p['eyr'] and re.match('^[0-9]{4}$', p['eyr']) and 2020 <= int(p['eyr']) <= 2030):
                    return False

                # hgt (Height) - a number followed by either cm or in:
                    # If cm, the number must be at least 150 and at most 193.
                    # If in, the number must be at least 59 and at most 76.
                flag = True
                if p['hgt']:
                    res = re.match('^([0-9]{2,3})(cm|in)$', p['hgt'])
                    if res:
                        unit = res.groups()[1]
                        val  = int(res.groups()[0])
                        if (unit == 'cm' and 150 <= val <= 193) or (unit == 'in' and 59 <= val <= 76):
                            flag = False
                if flag:
                    return False

                # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                if not (p['hcl'] and re.match('^#[0-9a-f]{6}$', p['hcl'])):
                    return False
                # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                if not (p['ecl'] and p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                    return False
                # pid (Passport ID) - a nine-digit number, including leading zeroes.
                if not (p['pid'] and re.match('^[0-9]{9}$', p['pid'])):
                    return False       
                # cid (Country ID) - ignored, missing or not.
                return True

            else:
                raise Exception("Invalid input: part == 1 or 2")

    batches  = []
    passport = Passport()
    for line in data:
        if len(line) > 1:
            line = line.strip()
            line = line.split(' ')
            for demo in line:
                key = demo.split(':')[0]
                val = demo.split(':')[1]
                passport.add_attr(key, val)
        else:
            if passport.is_valid(part):
                batches.append(passport)
            passport = Passport()

    if passport.is_valid(part):
        batches.append(passport)

    return len(batches)

def day_5(part, data):

    def get_seat_id(bsp:str, left:str, right:str, bound:tuple):
        bsp = bsp.strip()
        if not len(bsp) in [7, 3]:
            raise Exception(f"Invalid binary space partitioning length: {bsp}")
        
        rows = list(bound)
        for char in bsp:
            num_rows = rows[1] - rows[0] + 1
            if char == left:
                lower = rows[0]
                upper = rows[0] + (num_rows) // 2 - 1
                rows  = [lower, upper]
            elif char == right:
                lower = rows[0] + (num_rows) // 2
                upper = rows[1]
                rows  = [lower, upper]
            else:
                raise Exception(f"Invalid binary space partitioning input: {bsp}")
            # print(char, rows)
        
        if rows[0] != rows[1]:
            raise Exception(f"Invalid result: {bsp} -> {rows}")
            
        return rows[0]

    seats = []
    for line in data:
        line = line.strip()
        row  = get_seat_id(line[:7], 'F', 'B', (0, 127))
        col  = get_seat_id(line[7:], 'L', 'R', (0, 7))
        seat_id = row * 8 + col
        seats.append(seat_id)

    if part == 1:
        return max(seats)
    elif part == 2:
        seats.sort()
        for i in range(len(seats)-1):
            num = seats[i]
            if num + 2 == seats[i+1]:
                return num + 1

def day_6(part, data):

    def count_yes(group, part):
        num_passengers = len(group)
        group = "".join(group)
        group = Counter(group)
        if part == 1:
            return len(group)
        elif part == 2:
            return len([1 for val in group.values() if val == num_passengers])
                
    groups = []
    group  = []
    for line in data:
        line = line.strip()
        if line:
            group.append(line)
        else:
            groups.append(count_yes(group, part))
            group = []

    groups.append(count_yes(group, part))

    return sum(groups)

def day_7(part, data):

    if part == 1:
        # Create reverse graph
        g = defaultdict(set)
        src_pattern  = r'^([a-z ]+) bag'
        tgts_pattern = r'[0-9]+ ([a-z ]+) bag'
        for line in data:
            line = line.strip()
            src  = re.match(src_pattern, line).groups()[0]
            tgts = re.findall(tgts_pattern, line)
            for tgt in tgts:
                g[tgt].add(src)
        
        # BFS
        queue = deque(['shiny gold'])
        visited = set()
        while queue:
            node = queue.pop()
            visited.add(node)
            for tgt in g[node]:
                if tgt not in visited:
                    queue.append(tgt)

        return len(visited) - 1

    elif part == 2:
        # Create directed graph
        g = defaultdict(set)
        # Create bag count lookup
        bag_cost = defaultdict(int)

        src_pattern  = r'^([a-z ]+) bag'
        tgts_pattern = r'([0-9]+) ([a-z ]+) bag'
        for line in data:
            line = line.strip()
            src  = re.match(src_pattern, line).groups()[0]
            tgts = re.findall(tgts_pattern, line)
            for tgt in tgts:
                num_bags = int(tgt[0])
                bag_name = tgt[1]
                g[src].add((num_bags, bag_name))
                bag_cost[src] += num_bags
        
        # BFS
        queue   = deque(['shiny gold'])
        total   = 0
        while queue:
            node = queue.pop()
            total += bag_cost[node]
            print(node, total)
            for tgt in g[node]:
                num_bags = tgt[0]
                bag_name = tgt[1]
                for _ in range(num_bags):
                    queue.append(bag_name)

        return total


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
    print("Day {} Part {} Solution: {}".format(args.day, args.part, sol(args.part, data)))

