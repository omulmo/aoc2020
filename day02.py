

def isvalid1(line):
    arg1,arg2,password = line.split(' ')
    _min, _max = map(int, arg1.split('-'))
    _char = arg2[0]
    n = 0
    for c in password:
        if c==_char: n+=1
    return 1 if _min<=n and n<=_max else 0

def do1(inputs):
    return sum(map(isvalid1, inputs))

def isvalid2(line):
    arg1,arg2,password = line.split(' ')
    p1, p2 = map(int, arg1.split('-'))
    _char = arg2[0]

    n = sum(map(lambda x: 1 if x==_char else 0, (password[p1-1], password[p2-1])))

    return 1 if n==1 else 0


def do2(inputs):
    return sum(map(isvalid2, inputs))
