

DIRECTIONS = {
    'N': (0,1),
    'E': (1,0),
    'S': (0,-1),
    'W': (-1,0)
}


def go(directives):
    x,y=0,0
    nose='E'
    for directive in directives:
        direction, value = directive[0], int(directive[1:])
        if direction in 'LR':
            assert(value % 90 == 0)
            value=(-1 if direction=='L' else 1) * value//90
            nose = 'ESWN'[('ESWN'.index(nose) + value + 4) % 4]
            continue
        if direction not in 'NEWS':
            direction=nose
        dx,dy = DIRECTIONS[direction]
        x,y = x+value*dx, y+value*dy
    return x, y, nose


ROTATION = {
    0: (1,0,1,0),
    90: (0,1,0,-1),
    180: (-1,0,-1,0),
    270: (0,-1,0,1)
}

def go2(directives):
    x,y=0,0
    wpx,wpy=10,1
    for directive in directives:
        direction, value = directive[0], int(directive[1:])
        if direction=='F':
            x,y = x+value*wpx, y+value*wpy
        elif direction in 'LR':
            idx = 360 + (-1 if direction=='L' else 1) * value
            (xx,xy,yy,yx) = ROTATION[idx % 360]
            wpx, wpy = wpx*xx + wpy*xy, wpx*yx + wpy*yy 
        else:
            dx,dy = DIRECTIONS[direction]
            wpx,wpy = wpx+value*dx, wpy+value*dy
    return x, y



def do1(inputs):
    (x,y,nose) = go(inputs)
    return abs(x)+abs(y)

def do2(inputs):
    x,y = go2(inputs)
    return abs(x)+abs(y)
