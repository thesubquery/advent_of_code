# Python Standard Library

# pypi
import unittest

# Local
from aoc_2020 import *

class Test_aoc2020(unittest.TestCase):

    def test_day_1(self):
        data = get_input('data/2020/day_1.txt')
        
        # Part 1
        part = 1
        self.assertEqual(day_1(part, data), 888331)

        # Part 2
        part = 2
        self.assertEqual(day_1(part, data), 130933530)

    def test_day_2(self):
        data = get_input('data/2020/day_2.txt')
        
        # Part 1
        part = 1
        self.assertEqual(day_2(part, data), 445)

        # Part 2
        part = 2
        self.assertEqual(day_2(part, data), 491)
