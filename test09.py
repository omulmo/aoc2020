#!/usr/bin/env python3

from day09 import do1, do2, find_invalid, find_contiguous_sequence
import unittest

'''
'''

DATA = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''.splitlines()

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(127, find_invalid(DATA, 5) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(62, find_contiguous_sequence(127, DATA) )

if __name__=='__main__':
    unittest.main()
