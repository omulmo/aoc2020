from collections import defaultdict
import itertools
import re

def apply_bitmask(mask, value):
    result = [ i for i in value ]
    for i in range(36):
        if mask[i] in '01':
            result[i] = mask[i]
    return result

def get_addresses(mask, register):
    result = [ i for i in f'{register:036b}' ]
    qubits = []
    iterator=[]
    for (i,bit) in enumerate(mask):
        if bit=='X':
                qubits.append(i)
                iterator.append(('0','1'))
        if bit=='1':
            result[i] = '1'
    if len(qubits)==0:
        yield int(''.join(result),2)
    else:
        for combo in itertools.product(*iterator):
            for i,bit in enumerate(qubits):
                result[bit] = combo[i]
            yield int(''.join(result),2)


def do1(inputs):
    mem = {}
    mask = 'X'*36
    for instruction in inputs:
        (key,value) = instruction.split(' = ')
        if key=='mask':
            mask = value
            continue
        register = int(re.search('mem\[(\d+)\]', key).group(1))
        mem[register] = apply_bitmask(mask, f'{int(value):036b}')
    return sum([ int(''.join(v),2) for v in mem.values() ])

def do2(inputs):
    mem = {}
    mask = 'X'*36
    for instruction in inputs:
        (key,value) = instruction.split(' = ')
        if key=='mask':
            mask = value
            continue
        register = int(re.search('mem\[(\d+)\]', key).group(1))
        value = f'{int(value):036b}'
        for addr in get_addresses(mask, register):
            mem[addr] = value
    return sum([ int(''.join(v),2) for v in mem.values() ])
