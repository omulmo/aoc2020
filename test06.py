#!/usr/bin/env python3

from day06 import do1, do2
import unittest

'''
'''

DATA='''abc

a
b
c

ab
ac

a
a
a
a

b'''.splitlines()

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(11, do1(DATA) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(6, do2(DATA) )

if __name__=='__main__':
    unittest.main()
