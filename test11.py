#!/usr/bin/env python3

from day11 import do1, do2, next_state, find_end_state, problem1_ruleset, problem2_ruleset 
import unittest

'''
'''

STATE=['''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL''',
'''#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##''',
'''#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##''' ]

END_STATE = '''#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##'''

def to_array(state):
    return [ [i for i in row] for row in state.splitlines() ]


class Test1(unittest.TestCase):
    def testNextState(self):
        for i in range(len(STATE)-1):
            self.assertEqual(to_array(STATE[i+1]), next_state(STATE[i].splitlines(), problem1_ruleset) )
    def testEndState(self):
        self.assertEqual(to_array(END_STATE), find_end_state(STATE[0].splitlines(), problem1_ruleset) )
    def test1(self):
        self.assertEqual(37, do1(STATE[0].splitlines()) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(26, do2(STATE[0].splitlines()) )

if __name__=='__main__':
    unittest.main()
