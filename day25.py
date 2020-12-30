

def do1(inputs):
    card_pub = int(inputs[0])
    door_pub = int(inputs[1])
    loop_size = 0
    subject = 7
    value = 1
    while value not in [ card_pub, door_pub ]:
        value = (value * subject) % 20201227
        loop_size += 1
    print(f'loop size={loop_size}')

    subject = card_pub if value==door_pub else door_pub
    value = 1
    for _ in range(loop_size):
        value = (value * subject) % 20201227

    return value

def do2(inputs):
    return 0
