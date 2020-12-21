import sys, itertools


def add_rule(rules, line):
    (lhs,rhs) = line.split(': ')
    if rhs[0]=='"':
        value=rhs[1]
    else:
        value=[]
        for combo in rhs.split('|'):
            value.append(list(map(int, combo.strip().split(' '))))
    rules[int(lhs)] = value

def combo_match(rules, text, combo, pos):
    for rule in combo:
        pos = rule_match(rules, text, rule, pos)
        if pos<0: return -1
    return pos

def rule_match(rules, text, rule=0, pos=0):
    if pos>=len(text):
        return -1
    v = rules.get(rule, rule)
    if type(v)==str:
        n=len(v)
        return pos+n if pos+n<=len(text) and v==text[pos:pos+n] else -1
    for combo in v:
        p = combo_match(rules, text, combo, pos)
        if p>0:
            return p
    return -1


def do1(inputs):
    rules={}
    mode=1
    passed=0
    for line in inputs:
        if len(line)==0:
            mode=2
            continue
        if mode==1:
            add_rule(rules, line)
            continue
        if rule_match(rules, line)==len(line):
            passed += 1
    return passed


def all_combos(rules, rule):
    v = rules[rule]
    if type(v)==str:
        return {v}
    result_set = set()
    for combo in v:
        result = []
        for _rule in combo:
            result.append(all_combos(rules,_rule))
        for c in itertools.product(*result):
            result_set.add(''.join(c))
    return result_set

def all_combo_matches(rules, text, combo, positions):
    #print(f'all_combo: combo={combo} positions={positions}')
    for rule in combo:
        if len(positions)==0: break
        candidates=set()
        for pos in positions:
            candidates.update(all_rule_matches(rules, text, rule, pos))
        positions=candidates        
        #print(f'all_combos: positions={positions}')
    return positions

def all_rule_matches(rules, text, rule=0, pos=0):
    if pos>=len(text):
        return set()
    v = rules.get(rule, rule)
    result=set()
    if type(v)==str:
        n=len(v)
        if pos+n<=len(text) and v==text[pos:pos+n]:
            result.add(pos+n)
    else:
        for combo in v:
            result.update(all_combo_matches(rules, text, combo, {pos}))
    #print(f'all_rules: rule={rule} pos={pos} result={result}')
    return result


def fix_rules(rules):
    rules[42] = all_combos(rules,42)
    rules[31] = all_combos(rules,31)
    rules[8] = [[42], [42,8]]
    rules[11] = [[42,31], [42,11,31]]



def do2(inputs):
    rules={}
    mode=1
    passed=0
    for line in inputs:
        if len(line)==0:
            mode=2
            fix_rules(rules)
            continue
        if mode==1:
            add_rule(rules, line)
            continue
        v = all_rule_matches(rules, line)
        if len(line) in v:
            passed += 1
    return passed
