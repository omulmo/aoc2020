#!/usr/bin/env python3

from day02 import do1, do2
import unittest

'''
'''

DATA = '''1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''.splitlines()

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(2, do1(DATA) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(1, do2(DATA) )

if __name__=='__main__':
    unittest.main()
