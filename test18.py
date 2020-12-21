#!/usr/bin/env python3

from day18 import do1, do2, parse, parse2
import unittest

'''
'''

DATA = '''1 + 2 * 3 + 4 * 5 + 6
2 * 3 + (4 * 5)
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'''.splitlines()

class Test1(unittest.TestCase):
    def testParse(self):
        self.assertEqual(71, parse('1 + 2 * 3 + 4 * 5 + 6'))
        self.assertEqual(26, parse('2 * 3 + (4 * 5)'))
        self.assertEqual(13632, parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))
        self.assertEqual(12240, parse('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))

    def test1(self):
        self.assertEqual(71+26+13632+12240, do1(DATA) )

class Test2(unittest.TestCase):
    def testParse2(self):
        self.assertEqual(231, parse2('1 + 2 * 3 + 4 * 5 + 6'))
        self.assertEqual(51, parse2('1 + (2 * 3) + (4 * (5 + 6))'))
        self.assertEqual(1445, parse2('5 + (8 * 3 + 9 + 3 * 4 * 3)'))
        self.assertEqual(46, parse2('2 * 3 + (4 * 5)'))
        self.assertEqual(48, parse2('2 * 3 + (4 * 5) + 1'))
        self.assertEqual(669060, parse2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'))
        self.assertEqual(23340, parse2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'))
        self.assertEqual(168, parse2('(12*2)*2+5'))

if __name__=='__main__':
    unittest.main()
