#!/usr/bin/env python3

from d01 import do1, do2
import unittest

'''
'''

DATA = '''1721
979
366
299
675
1456'''.splitlines()

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(514579, do1(DATA) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(241861950, do2(DATA) )

if __name__=='__main__':
    unittest.main()
