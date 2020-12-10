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
    combinations = {0:1}
    for adapter_jolt in adapters:
        combos=0
        for jolt in range(max(0, adapter_jolt-3),adapter_jolt):
            combos += combinations.get(jolt, 0)
        combinations[adapter_jolt] = combos
    return combinations[computer_jolt]
