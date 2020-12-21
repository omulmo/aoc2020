#!/usr/bin/env python3

from day17 import do1, do2, Space, step
import unittest

'''
'''

DATA = '''.#.
..#
###'''.splitlines()

ITER1 = { -1: '''#..
..#
.#.'''.splitlines(),

0: '''#.#
.##
.#.'''.splitlines(),

1: '''#..
..#
.#.'''.splitlines()
}

class Test1(unittest.TestCase):
    def testIterator(self):
        space=Space(DATA)
        self.assertEqual((0,2), space.dimsizes[0])
        self.assertEqual((0,2), space.dimsizes[1])
        self.assertEqual((0,0), space.dimsizes[2])
        self.assertEqual(5, space.n_active())
        self.assertEqual(26, len(list(space.neighbors((1,2,3)))))

    def testSpace(self):
        space=Space(DATA)
        copy=Space()
        for pos in space.iterator():
            copy[pos]=space[pos]
        self.assertEqual(space.dimsizes, copy.dimsizes)
        self.assertEqual(space.n_active(), copy.n_active())

    def testStep(self):
        space=step(Space(DATA))
        self.assertEqual((0,2), space.dimsizes[0])
        self.assertEqual((1,3), space.dimsizes[1])
        self.assertEqual((-1,1), space.dimsizes[2])
        self.assertEqual(ITER1[-1], space.slice(-1))
        self.assertEqual(ITER1[0], space.slice(0))
        self.assertEqual(ITER1[1], space.slice(1))
        self.assertEqual(11, space.n_active())    

    def test1(self):
        self.assertEqual(112, do1(DATA) )

class Test2(unittest.TestCase):
    def testSpace(self):
        space=Space(DATA, dimensions=4)
        copy=Space(dimensions=space.dimensions)
        for pos in space.iterator():
            copy[pos]=space[pos]
        self.assertEqual(space.dimsizes, copy.dimsizes)
        self.assertEqual(space.n_active(), copy.n_active())

    def test2(self):
        self.assertEqual(848, do2(DATA) )

if __name__=='__main__':
    unittest.main()
