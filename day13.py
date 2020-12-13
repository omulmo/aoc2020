import sys

def do1(inputs):
    start=int(inputs[0])
    min_wait, best_busline = sys.maxsize, None
    for busline in map(int, filter(lambda x:x!='x', inputs[1].split(','))):
        wait = (busline - (start % busline)) % busline
        if wait<min_wait:
            min_wait, best_busline = wait, busline
    return min_wait * best_busline

def do2(inputs):
    n,modulo =1,0
    for (offset,value) in enumerate(inputs[1].split(',')):
        if value=='x': continue
        bus=int(value)
        for i in range(bus):
            if (modulo + n*i + offset) % bus == 0:
                modulo = modulo + n*i
                break
        n *= bus
    return modulo
