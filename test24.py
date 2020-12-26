#!/usr/bin/env python3

from day24 import do1, do2, coords, hex_neighbors
import unittest

'''
'''
DATA = '''sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew'''.splitlines()

class Test1(unittest.TestCase):
    def test1(self):
        self.assertEqual(10, do1(DATA) )

class Test2(unittest.TestCase):
    def testNbors(self):
        nbors = hex_neighbors((0,0))
        self.assertTrue(coords('ne') in nbors)
        self.assertTrue(coords('nw') in nbors)
        self.assertTrue(coords('e') in nbors)
        self.assertTrue(coords('w') in nbors)
        self.assertTrue(coords('se') in nbors)
        self.assertTrue(coords('sw') in nbors)

    def testNbors2(self):
        nbors = hex_neighbors((1,1))
        self.assertTrue(coords('nene') in nbors)
        self.assertTrue(coords('neenw') in nbors)
        self.assertTrue(coords('enee') in nbors)
        self.assertTrue(coords('ne') in nbors)
        self.assertTrue(coords('neese') in nbors)
        self.assertTrue(coords('e') in nbors)

    def test2(self):
        self.assertEqual(2208, do2(DATA) )

if __name__=='__main__':
    unittest.main()
