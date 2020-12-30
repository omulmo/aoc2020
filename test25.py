#!/usr/bin/env python3

from dayXX import do1, do2
import unittest

'''
'''

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(0, do1(None) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(0, do2(None) )

if __name__=='__main__':
    unittest.main()
