#!/usr/bin/env python3

from day03 import do1, do2
import unittest

'''
'''

DATA = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''.splitlines()

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(7, do1(DATA) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(336, do2(DATA) )

if __name__=='__main__':
    unittest.main()
