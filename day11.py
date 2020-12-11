import itertools

def problem1_ruleset(seat, occupied, empty):
    if seat=='L' and occupied==0:
        seat='#'
    elif seat=='#' and occupied>=4:
        seat='L'
    return seat

def problem2_ruleset(seat, occupied, empty):
    if seat=='L' and occupied==0:
        seat='#'
    elif seat=='#' and occupied>=5:
        seat='L'
    return seat


def next_state(room, ruleset, depth=1):
    w=len(room[0])
    h=len(room)
    result = [ ['x']*w for _ in range(h) ]
    for x,y in itertools.product(range(w), range(h)):
        seat = room[y][x]
        empty=0
        occupied=0
        for (dx,dy) in itertools.product((-1,0,1),(-1,0,1)):
            if (dx,dy) == (0,0): continue
            for distance in range(1,depth+1):
                i = x + dx*distance
                j = y + dy*distance
                if i<0 or i>=w: break
                if j<0 or j>=h: break
                if room[j][i]=='.': continue
                if room[j][i]=='#': occupied+=1
                if room[j][i]=='L': empty+=1
                break
        result[y][x] = ruleset(seat, occupied, empty)
    return result

def find_end_state(room, ruleset, depth=1):
    prev = None
    iterations=0
    while prev != room:
        prev=room
        room=next_state(room, ruleset, depth)
        iterations+=1
    return room

def room_to_array(room):
    w=len(room[0])
    h=len(room)
    return [ room[j][i] for i in range(w) for j in range(h) ]

def do1(inputs):
    return sum( [ 1 for _ in filter(lambda pos:pos=='#', room_to_array(find_end_state(inputs, problem1_ruleset))) ] )

def do2(inputs):
    return sum( [ 1 for _ in filter(lambda pos:pos=='#', room_to_array(find_end_state(inputs, problem2_ruleset, len(inputs)))) ] )
