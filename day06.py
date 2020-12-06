union = lambda a,b: b if a is None else a.union(b)
intersection = lambda a,b : b if a is None else a.intersection(b)

def group_answers(inputs, set_operation):
    group=None
    for answer in inputs:
        if len(answer)==0:
            yield group
            group=None
        else:
            group = set_operation(group, set(answer[:]))
    yield group


def do1(inputs):
    return sum(map(lambda x:len(x), group_answers(inputs, union)))

def do2(inputs):
    return sum(map(lambda x:len(x), group_answers(inputs, intersection)))
