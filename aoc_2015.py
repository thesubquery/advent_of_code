# Python Standard Library
import argparse
import os
import sys

from collections import Counter

# pypi

# Common

def get_input(file):
	with open(file, 'r') as f:
		data = f.readlines()
		data = [d.strip() for d in data]
		return data

def day_1(part, data):

	data = list(data[0])

	if part == 1:
		parenthesis = Counter(data)
		return parenthesis['('] - parenthesis[')']

	elif part == 2:
		counter = 0
		for i, bracket in enumerate(data):
			if bracket == '(':
				counter += 1
			elif bracket == ')':
				counter -= 1
			if counter == -1:
				return i + 1

def day_2(part, data):
	pass

def day_3(part, data):
	pass

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

