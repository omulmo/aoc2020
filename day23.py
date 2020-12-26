
def do1(inputs, rounds=100):
    deck=list(map(int,[i for i in inputs[0]]))
    n = len(deck)
    for _ in range(rounds):
        dst = deck[0]
        dst_idx = 0
        while dst_idx<4:
            dst = (dst-1) % n if dst>1 else n
            dst_idx = deck.index(dst)
        deck = deck[4:dst_idx+1] + deck[1:4] + deck[dst_idx+1:] + deck[0:1]
    first = deck.index(1)
    return ''.join(map(str, deck[first+1:] + deck[0:first]))


def do2(inputs, rounds=10_000_000):
    values = list(map(int, [i for i in inputs[0]]))
    n = 1_000_000
    cup_after = {}
    prev = values[0]
    for value in values[1:]:
        cup_after[prev] = value
        prev = value

    for value in range(max(values)+1, n+1):
        cup_after[prev] = value
        prev = value

    current = cup_after[n] = values[0]
    picked=[None,None,None]
    for round in range(rounds):
        if round%10000==0:
            print(f'round {round}: current={current}')
        q = current
        for i in range(3):
            q = cup_after[q]
            picked[i] = q

        card4 = cup_after[q]

        dst = (current-1) % n if current>1 else n
        while dst in picked:
            dst = (dst-1) % n if dst>1 else n

        cup_after[current] = card4
        cup_after[picked[2]] = cup_after[dst]
        cup_after[dst] = picked[0]
        current = cup_after[current]

    cup1 = cup_after[1]
    cup2 = cup_after[cup1]
    print(f'cup1={cup1} cup2={cup2}')
    return cup1 * cup2
