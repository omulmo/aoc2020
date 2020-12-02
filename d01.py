

def do1(inputs):
    candidates = set()
    for i in map(int, inputs):
        if i > 2020:
            continue
        if (2020-i) in candidates:
            return i * (2020-i)
        candidates.add(i)
    return 0

def do2(inputs):
    originals = set()
    candidates = {}
    numbers = list(map(int, inputs))
    for i in range(len(numbers)):
        a = numbers[i]
        if a > 2020:
            continue
        originals.add(a)
        for j in range(i+1, len(numbers)):
            b = numbers[j]
            c = a+b
            if c > 2020:
                continue
            if (2020-c) in originals:
                return a * b * (2020-c)
    return 0
