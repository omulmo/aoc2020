
def pair_product(_sum, numbers):
    candidates = set(filter(lambda x: x<_sum, numbers))
    for i in candidates:
        j = _sum - i
        if j in candidates:
            return i*j
    return 0

def do1(inputs):
    return pair_product(2020, map(int, inputs))

def do2(inputs):
    numbers = set(map(int, inputs))
    for i in numbers:
        if i > 2020:
            continue
        p = pair_product(2020-i, numbers)
        if p>0:
            return i*p
    return 0
