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

    def test_day_3(self):
        # Part 1
        part  = 1

        data  = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
        self.assertEqual(aoc2019.day_3(part, data), 6)
        data  = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
        self.assertEqual(aoc2019.day_3(part, data), 159)
        data  = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
        self.assertEqual(aoc2019.day_3(part, data), 135)                

        # Part 2
        part  = 2

        data  = ["R8,U5,L5,D3", "U7,R6,D4,L4"]
        self.assertEqual(aoc2019.day_3(part, data), 30)
        data  = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
        self.assertEqual(aoc2019.day_3(part, data), 610)
        data  = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]
        self.assertEqual(aoc2019.day_3(part, data), 410)            