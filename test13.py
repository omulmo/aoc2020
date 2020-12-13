#!/usr/bin/env python3

from day13 import do1, do2
import unittest

'''
'''

DATA='''939
7,13,x,x,59,x,31,19'''.splitlines()

DATA2 = [
    ('17,x,13,19', 3417),
    ('67,7,59,61', 754018),
    ('67,x,7,59,61', 779210),
    (DATA[1], 1068788),
    ('67,7,x,59,61', 1261476),
    ('1789,37,47,1889', 1202161486)
]

class Test1(unittest.TestCase):
    def test1(self): 
        self.assertEqual(295, do1(DATA) )

class Test2(unittest.TestCase):
    def test1(self):
            self.assertEqual(70147, do2(['foo', '7,13,x,x,59,x,31']) )
    def test2(self):
        for (line2, answer) in DATA2[0:1]:
            self.assertEqual(answer, do2(['foo', line2]) )

if __name__=='__main__':
    unittest.main()
