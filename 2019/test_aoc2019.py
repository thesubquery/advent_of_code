import unittest
import aoc2019

class Test_aoc2019(unittest.TestCase):

    def test_day_1(self):
        print("Hello World!")
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
        