from operator import mul
from copy import copy

def parse(inputs):
    n=(len(inputs)-3)//2
    return [ list(map(int, inputs[1:n+1])), list(map(int, inputs[n+3:])) ]

def combat(stacks):
    winner=None
    while True:
        for player in 0,1:
            if len(stacks[player])==0:
                winner = 1-player
        if winner!=None: break
        p1, p2 = stacks[0].pop(0), stacks[1].pop(0)
        won_round = 0 if p1>p2 else 1
        stacks[won_round].append(max(p1,p2))
        stacks[won_round].append(min(p1,p2))

    return stacks[winner]

def recursive_combat(stacks):
    seen_states=set()
    stack1, stack2 = stacks[0], stacks[1]
    while True:
        state=f'{stack1}:{stack2}'
        if state in seen_states: return 0
        seen_states.add(state)

        for player in 0,1:
            if len(stacks[player])==0: return 1-player

        p1, p2 = stack1.pop(0), stack2.pop(0)
        if len(stack1)>=p1 and len(stack2)>=p2:
            winner = recursive_combat([stack1[:p1], stack2[:p2]])
        else:
            winner = 0 if p1>p2 else 1

        stacks[winner].append(p1 if winner==0 else p2)
        stacks[winner].append(p1 if winner==1 else p2)


def do1(inputs):
    stack = combat(parse(inputs))
    return sum(map(mul, stack, range(len(stack),0,-1)))

def do2(inputs):
    stacks = parse(inputs)
    winner=recursive_combat(stacks)
    stack = stacks[winner]
    return sum(map(mul, stack, range(len(stack),0,-1)))
