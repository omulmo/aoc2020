#!/usr/bin/env python3

from day23 import do1, do2
import unittest

'''
'''

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual('92658374', do1(['389125467'], rounds=10) )
        self.assertEqual('67384529', do1(['389125467']) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(149245887792, do2(['389125467']) )

if __name__=='__main__':
    unittest.main()
