from collections import defaultdict

class SetWithWeights:
    def __init__(self):
        self.set = defaultdict(lambda: 0)
    def add(self, _set):
        for x in _set:
            self.set[x] += 1
    def remove(self, _set):
        for x in _set:
            self.set[x] -= 1
    def has(self, x):
        return x in self.set and self.set[x]>0

class ListItem:
    def __init__(self, value, _set):
        self.value = value
        self.set = _set

def find_invalid(inputs, preamble=25):
    numbers = list(map(int, inputs))
    items = [ ListItem(i, set()) for i in numbers[:preamble] ]
    for i in range(preamble):
        item = items[i]
        for j in range(i+1,preamble):
            item.set.add(item.value+numbers[j])

    total = SetWithWeights()
    for item in items:
        total.add(item.set)

    for num in numbers[preamble:]:
        if not total.has(num):
            return num
        _newset = set()
        for item in items:
            _newset.add(num+item.value)
        items.append(ListItem(num,_newset))
        total.add(_newset)
        first = items.pop(0)
        total.remove(first.set)
    return -1

def find_contiguous_sequence(target, inputs):
    numbers=list(map(int, inputs))
    for i in range(len(numbers)-1,0,-1):
        if numbers[i]>target:
            continue
        total=numbers[i]
        j=i-1
        while total<target and j>=0:
            total += numbers[j]
            if total==target:
                print(f'found sequence {j}:{numbers[j]} -> {i}:{numbers[i]}')
                sequence = numbers[j:i+1]
                return min(sequence) + max(sequence)
            j -= 1
    return -1
        
def do1(inputs):
    return find_invalid(inputs)

def do2(inputs):
    return find_contiguous_sequence(find_invalid(inputs), inputs)
