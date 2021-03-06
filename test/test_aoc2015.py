# Python Standard Library

# pypi
import unittest

# Local
from aoc_2015 import *

class Test_aoc2015(unittest.TestCase):

    def test_day_1(self):
        data = get_input('data/2015/day_1.txt')
        
        # Part 1
        part = 1
        self.assertEqual(day_1(part, data), 232)

        # Part 2
        part = 2
        self.assertEqual(day_1(part, data), 1783)
