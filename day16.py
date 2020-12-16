from collections import defaultdict
from typing import ValuesView

def parse(inputs):
    fields={}
    my_ticket=None
    nearby_tickets=[]
    state=1
    for line in inputs:
        if line=='':
            state += 1
            continue
        if line.endswith(':'): continue
        if state==1:
            (key,values) = line.split(': ')
            fields[key] = v = []
            for value in values.split(' or '):
                min,max = map(int, value.split('-'))
                v.append((min,max))
        else:
            ticket=list(map(int, line.split(',')))
            if state==2:
                my_ticket=ticket
            else:
                nearby_tickets.append(ticket)
    return fields, my_ticket, nearby_tickets


def test_number(number, array_of_ranges):
    for r in array_of_ranges:
        for (min,max) in r:
            if number < min:
                continue
            if number <= max:
                return True
    return False

def test_ticket(ticket, all_ranges):
    ok=True
    i=0
    while ok and i<len(ticket):
        ok = test_number(ticket[i], all_ranges)
        i += 1
    return ok


def do1(inputs):
    (fields,_,nearby_tickets) = parse(inputs)
    all_ranges = list(fields.values())
    invalid_entries=[]
    for ticket in nearby_tickets:
        for field in ticket:
            if not test_number(field, all_ranges):
                invalid_entries.append(field)
    return sum(invalid_entries)


def do2(inputs):
    (fields,my_ticket,nearby_tickets) = parse(inputs)
    all_ranges = list(fields.values())
    valid_tickets = list(filter(lambda t: test_ticket(t, all_ranges), nearby_tickets))
    print(f'found {len(nearby_tickets) - len(valid_tickets)} invalid tickets')
    field_columns=defaultdict(lambda: set())
    for (field,ranges) in fields.items():
        for col in range(len(my_ticket)):
            if all(map(lambda ticket: test_number(ticket[col], [ranges]), valid_tickets)):
                field_columns[field].add(col)

    old=field_columns
    print(old)
    queue = list(old.keys())
    while len(queue)>0:
        field = queue.pop(0)
        columns = old[field]
        if len(columns)>1: continue
        print(f'reduction: {field} = {columns}')
        new = {}
        for f in old.keys():
            new[f] = diff = old[f].difference(columns) if f!=field else old[f]            
            if diff != old[f]:
                queue.append(f)
        old = new
        print(old)

    print(my_ticket)    
    result=1
    for (field,column) in filter(lambda item:item[0].startswith('departure'), old.items()):
        col = column.pop()
        result *= my_ticket[col]
        print(f'field {field} -> {col} -> {my_ticket[col]} sum={result}')
    return result
