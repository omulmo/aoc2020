#!/usr/bin/env python3

from day10 import do1, do2
import unittest

'''
'''

DATA = '''16
10
15
5
1
11
7
19
6
12
4'''.splitlines()

DATA2 = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''.splitlines()


class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(7*5, do1(DATA) )
    def test2(self):
        self.assertEqual(22*10, do1(DATA2) )

class Test2(unittest.TestCase):
    def test1(self):
        self.assertEqual(8, do2(DATA) )
    def test2(self):
        self.assertEqual(19208, do2(DATA2) )

if __name__=='__main__':
    unittest.main()
