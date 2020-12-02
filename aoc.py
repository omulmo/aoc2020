#! /usr/bin/env python3

import sys
import importlib

if __name__=='__main__':
    if len(sys.argv) < 3:
        print('Syntax: aoc <day> <1|2> [input]')
        print('default input file is <day>.txt')
        sys.exit(1)

    (day, star) = map(int, sys.argv[1:3])

    filename = f'{day:02d}.txt' if len(sys.argv)==3 else sys.argv[3]

    module = importlib.import_module(f'day{day:02d}')

    inputs = []
    for line in sys.stdin if filename=='-' else open(filename):
        inputs.append( line.strip() )

    print(module.do1(inputs) if star==1 else module.do2(inputs))
