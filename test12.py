#!/usr/bin/env python3

from day12 import do1, do2, go, go2
import unittest

'''
'''

DATA = '''F10
N3
F7
R90
F11'''.splitlines()

class Test1(unittest.TestCase):
    def testGo(self):
        self.assertEqual((3,2,'E'), go(['F3','N2']))
        self.assertEqual((-1,0,'W'), go(['L180','F1']))
        self.assertEqual((-1,-2,'W'), go(['R180','F1','S2']))
        self.assertEqual((-1,-3,'W'), go(['R90','F3','L270','W1']))
    def test1(self):
        self.assertEqual(25, do1(DATA) )

class Test2(unittest.TestCase):
    def testGo2(self):
        self.assertEqual((214,-72), go2(DATA) )
    def testRot(self):
        self.assertEqual((10,1), go2(['R0','F1']) )
        self.assertEqual((1,-10), go2(['R90','F1']) )
        self.assertEqual((-10,-1), go2(['R180','F1']) )
        self.assertEqual((-1,10), go2(['R270','F1']) )
        self.assertEqual(go2(['R90','F1']), go2(['L270','F1']) )
    def test2(self):
        self.assertEqual(286, do2(DATA) )

if __name__=='__main__':
    unittest.main()
