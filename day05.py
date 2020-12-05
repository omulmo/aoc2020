def seat_number(_str):
    row = int(_str[:7].replace('B','1').replace('F','0'), 2)
    col = int(_str[7:].replace('R','1').replace('L','0'), 2)
    return row * 8 + col

def do1(inputs):
    return max(map(seat_number, inputs))

def do2(inputs):
    seats = set(map(seat_number, inputs))
    _min = min(seats)
    _max = max(seats)
    missing = set(i for i in range(_min,_max+1)) - seats
    return missing.pop()
