from collections import defaultdict

def coords(instruction):
    x = y = 0
    seq = iter(instruction)
    for ch in seq:
        if ch in 'ns':
            y += 1 if ch=='n' else -1
            ch = next(seq)
            if y%2 == 0:
                x += 1 if ch=='e' else 0
            else:
                x -= 1 if ch=='w' else 0
        else:
            x += 1 if ch=='e' else -1

    return x,y

def hex_neighbors(pos):
    x,y = pos
    xl,xr = (x-1,x) if y%2==0 else (x,x+1)
    return (x-1,y), (x+1,y), (xl,y-1), (xr,y-1), (xl,y+1), (xr,y+1)


def do1(inputs):
    tiles = defaultdict(lambda: False)
    for pos in map(coords, inputs):
        tiles[pos] = not tiles[pos]

    return sum([ 1 for _ in filter(None, tiles.values())])

def do2(inputs):
    all_tiles = set()
    tiles = defaultdict(lambda: False)
    for pos in map(coords, inputs):
        all_tiles.add(pos)
        tiles[pos] = not tiles[pos]

    for day in range(100):
        for tile in tiles.keys():
            for nbor in hex_neighbors(tile):
                all_tiles.add(nbor)

        new_pattern = defaultdict(lambda: False)
        for pos in all_tiles:
            is_black = tiles[pos]
            n_black = sum(filter(None, [tiles[nbor] for nbor in hex_neighbors(pos)]))
            if is_black:
                flipped = n_black==0 or n_black>2
            else:
                flipped = n_black==2

            new_pattern[pos] = not is_black if flipped else is_black
        tiles = new_pattern
    return sum([ 1 for _ in filter(None, tiles.values())])