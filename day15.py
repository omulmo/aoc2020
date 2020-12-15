from collections import defaultdict

def doit(inputs, end_turn=2020):
    spoken = {}
    turn=1
    prev=-1
    for number in map(int, inputs[0].split(',')):
        spoken[prev] = turn
        prev=number
        turn += 1
    while turn<=end_turn:
        number = (turn-spoken[prev]) if prev in spoken else 0
        spoken[prev] = turn
        #print(f'turn {turn} : prev={prev} spoken={number}')
        prev=number
        turn += 1
    return prev

def do1(inputs):
    return doit(inputs)

def do2(inputs):
    return doit(inputs, end_turn=30_000_000)
