#!/usr/bin/env python3

from day16 import do1, do2
import unittest

'''
'''

DATA = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''.splitlines()

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(71, do1(DATA) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(0, do2(DATA) )

if __name__=='__main__':
    unittest.main()
