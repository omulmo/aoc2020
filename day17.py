import itertools
import sys

class Space:
    def __init__(self, z0slice=['.'], dimensions=3):
        self.active = set()
        self.dimensions=dimensions
        self.dimsizes=[(sys.maxsize,-sys.maxsize)]*dimensions
        for (y,line) in enumerate(z0slice):
            for (x,item) in enumerate(line):
                pos = tuple([x,y] + [0]*(dimensions-2))
                self[pos] = item

    def __getitem__(self, pos):
        return '#' if pos in self.active else '.'

    def __setitem__(self, pos, value):
        if value=='#':
            self.active.add(pos)
            for (dim,value) in enumerate(pos):
                _min,_max = self.dimsizes[dim]
                self.dimsizes[dim]=(min(_min,value),max(_max,value))

    def iterator(self):
        rng = lambda mi,ma: range(mi-1,ma+2)
        ranges = [ rng(*minmax) for minmax in self.dimsizes ]
        return itertools.product(*ranges)

    def neighbors(self, pos):
        rng = [(-1,0,1)]*self.dimensions
        for diff in itertools.product(*rng):
            npos = tuple(map(sum, zip(pos,diff)))
            if npos==pos: continue
            yield npos

    def slice(self, z):
        result=[]
        xmin,xmax = self.dimsizes[0]
        ymin,ymax = self.dimsizes[1]
        added_dimensions = self.dimensions-3
        for y in range(ymin,ymax+1):
            line=''
            for x in range(xmin,xmax+1):
                line += self[tuple([x,y,z]+[0]*added_dimensions)]
            result.append(line)
        return result

    def n_active(self):
        return len(self.active)


def step(space):
    result=Space(dimensions=space.dimensions)
    for pos in space.iterator():
        n_active = len(space.active.intersection(space.neighbors(pos)))
        if pos in space.active:
            is_active = n_active==2 or n_active==3
        else:
            is_active = n_active==3
        result[pos] = '#' if is_active else '.'
    return result




def do1(inputs):
    space=Space(inputs)
    for iteration in range(1,7):
        space=step(space)
        print(f'iteration {iteration} : {space.n_active()}')
    return space.n_active()


def do2(inputs):
    space=Space(inputs,dimensions=4)
    for iteration in range(1,7):
        space=step(space)
        print(f'iteration {iteration} : {space.n_active()}')
    return space.n_active()
