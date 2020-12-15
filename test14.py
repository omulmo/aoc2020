#!/usr/bin/env python3

from day14 import do1, do2
import unittest

'''
'''

DATA = '''mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0'''.splitlines()

DATA2 = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''.splitlines()

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(165, do1(DATA) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(208, do2(DATA2) )

if __name__=='__main__':
    unittest.main()
