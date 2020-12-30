from collections import defaultdict
from functools import reduce
from operator import mul

class Tile:
    def __init__(self, id, image):
        self.id = id
        self.image = image
        self.rotation = 0
        self._update_borders()
        self.nbors = set()

    def _update_borders(self):
        n = len(self.image)-1
        self.borders={
            'n':self.image[0],
            's':self.image[n][::-1],
            'e':''.join([ x[n] for x in self.image ]),
            'w':''.join([ x[0] for x in self.image ])[::-1]
        }

    def cutout(self):
        n = len(self.image)-1
        return [ self.image[i][1:-1] for i in range(1,n) ]

    def flip(self):
        self.rotation = (self.rotation + 4) % 8
        for i,row in enumerate(self.image):
            self.image[i] = row[::-1]
        self._update_borders()

    def rotate(self):
        n = len(self.image)-1
        self.rotation = (4 if self.rotation > 3 else 0) + (self.rotation + 1) % 4
        self.image = [ ''.join([ self.image[i][j] for i in range(n,-1,-1) ]) for j in range(0,n+1) ]
        self._update_borders()

    def set_rotation(self, new_rotation):
        while self.rotation != new_rotation:
            if abs(self.rotation - new_rotation) >= 4:
                self.flip()
            else:
                self.rotate()

    def __repr__(self):
        return f'Tile {self.id} rotation={self.rotation}'


def parse(inputs):
    tiles=[]
    for idx in range(0, len(inputs),12):
        tile_id = int(inputs[idx].replace(':','').split(' ')[1])
        tiles.append(Tile(tile_id,inputs[idx+1:idx+11]))
    return tiles


def find_neighbors(tiles):
    signatures = defaultdict(lambda: set())
    for tile in tiles:
        for border in tile.borders.values():
            signatures[border].add(tile)
            signatures[border[::-1]].add(tile)

    for ids in signatures.values():
        if len(ids)==2:
            t1,t2 = ids
            t1.nbors.add(t2)
            t2.nbors.add(t1)

    return tiles


def do1(inputs):
    tiles = find_neighbors(parse(inputs))
    corner_tiles = set(filter(lambda tile: len(tile.nbors)==2, tiles))
    assert(len(corner_tiles)==4)
    return reduce(mul, map(lambda tile: tile.id, corner_tiles))


DIRECTION = {
    'n': (0,-1,'s'),
    'e': (1,0,'w'),
    'w': (-1,0,'e'),
    's': (0,1,'n')
}

def verify_tile_alignment(grid, x, y):
    dim = len(grid)
    tile = grid[y][x]
    for direction in 'news':
        dx,dy,opposite = DIRECTION[direction]
        nbx, nby = x+dx, y+dy
        if min(nbx,nby)<0: continue
        if max(nbx,nby)>=dim: continue
        nbor_tile = grid[nby][nbx]
        if nbor_tile==None: continue
        if nbor_tile.borders[opposite][::-1] != tile.borders[direction]:
            return False
    return True

def fill_grid(grid, xy, tiles):
    dim = len(grid)
    if xy==dim*dim: return True
    x, y = xy%dim, xy//dim
    nbors = 4
    if x==0 or x==dim-1: nbors -= 1
    if y==0 or y==dim-1: nbors -= 1
    candidate_tiles = set(filter(lambda tile: len(tile.nbors)==nbors, tiles))
    for tile in candidate_tiles:
        grid[y][x] = tile
        remaining_tiles = tiles - {tile}
        for rotation in range(0,8):
            tile.set_rotation(rotation)
            if verify_tile_alignment(grid, x, y) and fill_grid(grid, xy+1, remaining_tiles):
                return True
        grid[y][x] = None
    return False


def get_image(inputs):
    tiles = set(find_neighbors(parse(inputs)))

    dim = int(len(tiles)**0.5)
    assert(dim*dim==len(tiles))

    grid = [ [ None ] * dim for _ in range(dim) ]

    assert(fill_grid(grid, 0, tiles))

    for y in range(dim):
        print(' '.join([ f'{x.id} rot={x.rotation}' for x in grid[y]]))

    img = ['']*8*dim
    for y in range(dim):
        for x in range(dim):
            cutout = grid[y][x].cutout()
            #print(f'{x}, {y}:')
            #print('\n'.join(cutout))
            #print()
            for i in range(8):
                img[y*8+i] += cutout[i]
    return img


SEA_MONSTER = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.splitlines()

SEA_MONSTER_COORDS = set()
for y in range(len(SEA_MONSTER)):
    for x,item in enumerate(SEA_MONSTER[y]):
        if item=='#': SEA_MONSTER_COORDS.add((x,y))

def find_seamonsters(image):
    dim=len(image)
    width=len(SEA_MONSTER[0])
    height=len(SEA_MONSTER)
    monsters_found=0
    for y in range(dim-height):
        for x in range(dim-width):
            count=0
            for dx,dy in SEA_MONSTER_COORDS:
                if image[y+dy][x+dx]=='#': count+=1
            if count==len(SEA_MONSTER_COORDS):
                monsters_found+=1
                print(f'Sea monster found at {x},{y}')
    return monsters_found

def do2(inputs):
    tile = Tile(101, get_image(inputs))
    monsters=-1
    for rotation in range(8):
        tile.set_rotation(rotation)
        n = find_seamonsters(tile.image)
        print(f'rotation={rotation} sea monsters={n}')
        monsters=max(monsters, n)

    hashes = len(''.join([ line.replace('.','') for line in tile.image]))
    return hashes - monsters*len(SEA_MONSTER_COORDS)
