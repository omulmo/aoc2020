
def parse(inputs):
    program=[]
    for line in inputs:
        (op,num) = line.split(' ')
        program.append((op, int(num)))
    return program

def run(program):
    ptr = 0
    value = 0
    visited = set()
    done = False
    loop = False
    while not loop and not done:
        visited.add(ptr)
        (op,num) = program[ptr]
        if op=="nop":
            ptr += 1
        if op=="acc":
            value += num
            ptr += 1
        if op=="jmp":
            ptr += num
        loop = ptr in visited
        done = ptr >= len(program)
    if loop:
        print(f'loop at {ptr}')
    return loop, value


def do1(inputs):
    return run(parse(inputs))

def do2(inputs):
    program = parse(inputs)
    for i,(op,num) in enumerate(program):
        if i=="acc":
            continue
        program[i] = ("jmp" if op=="nop" else "nop",num)
        (loop,value) = run(program)
        if not loop:
            return value
        program[i] = (op,num)
    return 0
