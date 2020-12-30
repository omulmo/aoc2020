#!/usr/bin/env python3

from day20 import do1, do2, parse, Tile, get_image
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

IMAGE = '''.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###'''.splitlines()

class Test1(unittest.TestCase):
    def testParse(self):
        tiles = parse(DATA)
        self.assertEqual(9, len(tiles))
        tile9 = tiles[8]
        self.assertEqual(3079, tile9.id)
        self.assertEqual(DATA[-1][::-1], tile9.borders['s'])
        
    def testTile(self):
        tile = Tile(101, DATA[1:11])
        self.assertEqual('..##.#..#.', tile.borders['n'])
        self.assertEqual('...#.##..#', tile.borders['e'])
        self.assertEqual('###..###..', tile.borders['s'])
        self.assertEqual('.#..#####.', tile.borders['w'])

    def testRotate(self):
        tile = Tile(101, DATA[1:11])
        tile.rotate()
        self.assertEqual(1, tile.rotation)
        self.assertEqual('.#..#####.', tile.borders['n'])
        self.assertEqual('..##.#..#.', tile.borders['e'])
        self.assertEqual('...#.##..#', tile.borders['s'])
        self.assertEqual('###..###..', tile.borders['w'])
        tile.rotate()
        self.assertEqual(2, tile.rotation)
        self.assertEqual('###..###..', tile.borders['n'])
        self.assertEqual('.#..#####.', tile.borders['e'])
        self.assertEqual('..##.#..#.', tile.borders['s'])
        self.assertEqual('...#.##..#', tile.borders['w'])
        tile.rotate()
        tile.rotate()
        self.assertEqual(0, tile.rotation)
        self.assertEqual('###..###..', tile.borders['s'])
        self.assertEqual('..##.#..#.', tile.borders['n'])
        self.assertEqual('...#.##..#', tile.borders['e'])
        self.assertEqual('.#..#####.', tile.borders['w'])

    def testFlip(self):
        tile = Tile(101, DATA[1:11])
        tile.flip()
        self.assertEqual(4, tile.rotation)
        self.assertEqual('..##.#..#.'[::-1], tile.borders['n'])
        self.assertEqual('...#.##..#'[::-1], tile.borders['w'])
        self.assertEqual('###..###..'[::-1], tile.borders['s'])
        self.assertEqual('.#..#####.'[::-1], tile.borders['e'])

    def testSetRotate(self):
        tile1 = Tile(101, DATA[1:11])
        tile2 = Tile(101, DATA[1:11])
        tile3 = Tile(101, DATA[1:11])
        tile2.flip()
        tile2.rotate()
        tile2.rotate()
        tile1.set_rotation(6)
        self.assertEqual(tile1.rotation, tile2.rotation)
        self.assertEqual(tile1.image, tile2.image)
        self.assertEqual(tile1.borders, tile2.borders)
        tile1.set_rotation(1)
        tile3.rotate()        
        self.assertEqual(tile1.image, tile3.image)


    def test1(self):
        self.assertEqual(20899048083289, do1(DATA) )

class Test2(unittest.TestCase):
    def testImage(self):
        tile = Tile(101, get_image(DATA))
        success=False
        for rotation in range(8):
            tile.set_rotation(rotation)
            if (tile.image==IMAGE):
                success = True
        self.assertTrue(success)
        
    def test2(self):
        self.assertEqual(273, do2(DATA) )

if __name__=='__main__':
    unittest.main()
