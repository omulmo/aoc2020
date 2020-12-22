#!/usr/bin/env python3

from day22 import do1, do2
import unittest

'''
'''

DATA = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''.splitlines()

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(306, do1(DATA) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(291, do2(DATA) )

if __name__=='__main__':
    unittest.main()
