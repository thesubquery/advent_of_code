import argparse
import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(prog='argparse_testing',
                                    description='List the content of a folder')
    # prog - name of the program. sys. By default, the library uses the value of 
    # the sys.argv[0] element to set the name of the program, which as you probably 
    # already know is the name of the Python script you have executed. However, you 
    # can specify the name of your program just by using the prog keyword:

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))