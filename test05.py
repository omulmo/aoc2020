#!/usr/bin/env python3

from day05 import do1, do2, seat_number
import unittest

'''
'''

SEATS = {
    "BFFFBBFRRR": { "row":70, "col":7, "id": 567 },
    "FFFBBBFRRR": { "row":14, "col":7, "id": 119 },
    "BBFFBBFRLL": { "row":102, "col":4, "id":820 }
}

class Test1(unittest.TestCase):
    def testParser(self):
        self.assertEqual(567, seat_number("BFFFBBFRRR") )
    def test1(self):
        self.assertEqual(820, do1(list(SEATS.keys())) )

if __name__=='__main__':
    unittest.main()
