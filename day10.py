from collections import defaultdict

def do1(inputs):
    adapters = sorted(map(int, inputs))
    diff={1:0, 2:0, 3:1}
    prev=0
    for adapter in adapters:
        assert(1<=adapter-prev<=3)
        diff[adapter-prev] += 1
        prev=adapter
    return diff[1]*diff[3]

def do2(inputs):
    adapters = sorted(map(int, inputs))
    computer_jolt = adapters[-1]+3
    adapters.append(computer_jolt)
    adapters.insert(0,0)
    combinations = {}
    for adapter in adapters:
        combos=0
        for jolt in range(max(0, adapter-3),adapter):
            combos += combinations.get(jolt, 0)
        combinations[adapter] = max(1,combos)
    return combinations[computer_jolt]
