#!/usr/bin/env python3

from day20 import do1, do2, parse, arrange, Tile
import unittest

'''
'''

DATA = '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...'''.splitlines()

class Test1(unittest.TestCase):
    def testParse(self):
        tiles = parse(DATA)
        self.assertEqual(9, len(tiles))
        tile9 = tiles[8]
        self.assertEqual(3079, tile9.id)
        self.assertEqual(DATA[-1][::-1], tile9.borders['s'])
        
    def testTile(self):
        tile = Tile(101, DATA[1:11])
        self.assertEqual('###..###..', tile.borders['s'])
        self.assertEqual('..##.#..#.', tile.borders['n'])
        self.assertEqual('...#.##..#', tile.borders['e'])
        self.assertEqual('.#..#####.', tile.borders['w'])

        self.assertEqual(tile.borders['n'], tile.border(0,'n'))
        self.assertEqual(tile.borders['s'], tile.border(0,'s'))
        self.assertEqual(tile.borders['w'], tile.border(0,'w'))
        self.assertEqual(tile.borders['e'], tile.border(0,'e'))


    def test1(self):
        self.assertEqual(20899048083289, do1(DATA) )

class Test2(unittest.TestCase):
    def test2(self):
        self.assertEqual(0, do2(None) )

if __name__=='__main__':
    unittest.main()
