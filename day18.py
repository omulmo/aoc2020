import string
from operator import add, mul

def tokenize(line):
    line=''.join(line.split(' '))
    digits=''
    for item in line:
        if item in string.digits:
            digits += item
            continue
        else:
            if len(digits)>0:
                yield int(digits)
                digits=''
            yield item
    if len(digits)>0:
        yield int(digits)

def tree(tokens):
    ack=0
    op=add
    for token in tokens:
        if token=='(':
            ack = op(ack,tree(tokens))
            continue
        if token==')':
            return ack
        if type(token)==int:
            ack = op(ack,token)
            continue
        if token=='+':
            op=add
            continue
        if token=='*':
            op=mul
    return ack


def tree2(tokens, depth=0):
    ack=0
    for token in tokens:
        #print(f'{" "*depth} token={token} ack={ack}')
        if token=='(':
            (val,eop) = tree2(tokens, depth+2)
            assert(eop)
            ack += val
            continue
        if token==')':
            return ack, True
        if type(token)==int:
            ack += token
            continue
        if token=='+':
            continue
        if token=='*':
            (val,eop) = tree2(tokens, depth)
            ack *= val
            if eop:
                return ack, True           
    #print(f'{" "*depth} done ack={ack}')
    return ack, False

def parse(line):
#    p,value = evaluate(line+'$', 0)
#    return value
    return tree(tokenize(line))

def parse2(line):
    (val,t)= tree2(tokenize(line))
    return val

def do1(inputs):
    return sum(map(parse, inputs))

def do2(inputs):
    return sum(map(parse2, inputs))
