import unittest
import aoc2019
from intcode import Intcode

class Test_aoc2019(unittest.TestCase):

    def test_day_1(self):
        # Part 1
        data = [12]
        self.assertEqual(aoc2019.day_1(1, data), 2)
        data = [14]
        self.assertEqual(aoc2019.day_1(1, data), 2)
        data = [1969]
        self.assertEqual(aoc2019.day_1(1, data), 654)
        data = [100756]
        self.assertEqual(aoc2019.day_1(1, data), 33583)

        # Part 2
        data = [14]
        self.assertEqual(aoc2019.day_1(2, data), 2)
        data = [1969]
        self.assertEqual(aoc2019.day_1(2, data), 966)
        data = [100756]
        self.assertEqual(aoc2019.day_1(2, data), 50346)

    def test_day_2(self):

        def run_intcode(data):
            data    = [str(each) for each in data]
            program = Intcode(data)
            program.run(None)
            return [int(each) for each in program.data]
        # Part 1
        data = run_intcode([1,0,0,0,99])
        self.assertEqual(data, [2,0,0,0,99])
        data = run_intcode([2,3,0,3,99])
        self.assertEqual(data, [2,3,0,6,99])
        data = run_intcode([2,4,4,5,99,0])
        self.assertEqual(data, [2,4,4,5,99,9801])
        data = run_intcode([1,1,1,4,99,5,6,0,99])
        self.assertEqual(data, [30,1,1,4,2,5,6,0,99])                
       
        