from collections import defaultdict
from functools import reduce
from operator import mul

class Tile:
    def __init__(self, id, image):
        self.id = id
        self.borders={
            'n':image[0],
            's':image[9][::-1],
            'e':''.join([ x[9] for x in image ]),
            'w':''.join([ x[0] for x in image ])[::-1]
        }
        self.nbors = set()

    def border(self, config, face):
        rotation = config % 4
        clockwise = config % 2 == 0
        order = ('nwsenws' if clockwise else 'neswnes')[rotation:rotation+4]
        face_index = 'nesw'.index(face)
        signature = self.borders[order[face_index]]
        return signature if clockwise else signature[::-1]

    def __repr__(self):
        return f'Tile {self.id}'


def parse(inputs):
    tiles=[]
    for idx in range(0, len(inputs),12):
        tile_id = int(inputs[idx].replace(':','').split(' ')[1])
        tiles.append(Tile(tile_id,inputs[idx+1:idx+11]))
    return tiles

def arrange(tiles):
    dim = int(len(tiles)**0.5)
    assert(dim*dim == len(tiles))
    square=[[i*3+j for j in range(dim)] for i in range(dim) ]
    
    lookup = dict(map(lambda tile: (tile.id, tile), tiles))

    fingerprints = defaultdict(lambda: set())
    for tile in tiles:
        for border in tile.borders.values():
            fingerprints[border].add(tile.id)
            fingerprints[border[::-1]].add(tile.id)

    for ids in fingerprints.values():
        if len(ids)==2:
            t1,t2 = ids
            lookup[t1].nbors.add(t2)
            lookup[t2].nbors.add(t1)

    corners = set(filter(lambda tile: len(tile.nbors)==2, tiles))
    assert(len(corners)==4)

    edges = set(filter(lambda tile: len(tile.nbors)==3, tiles))
    assert(len(edges)==4*(dim-2))

    middle = set(filter(lambda tile: len(tile.nbors)==4, tiles))
    assert(len(middle)==(dim-2)*(dim-2))

    return reduce(mul, map(lambda x: x.id, corners))


def do1(inputs):
    return arrange(parse(inputs))

def do2(inputs):
    return 0
