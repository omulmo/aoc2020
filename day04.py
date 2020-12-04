import re

def interval(x, _min, _max):
    return _min<=int(x) and int(x)<=_max

def height(x):
    if x[-2:]=='in':
        return interval(x[:-2], 59, 76)
    if x[-2:]=='cm':
        return interval(x[:-2], 150, 193)
    return False

MANDATORY_FIELDS = {
    'byr': lambda x: interval(x, 1920, 2002),
    'iyr': lambda x: interval(x, 2010, 2020),
    'eyr': lambda x: interval(x, 2020, 2030),
    'hgt': lambda x: height(x),
    'hcl': lambda x: re.fullmatch('^#[0-9a-f]{6}$', x) != None,
    'ecl': lambda x: x in ('amb','blu','brn','gry','grn','hzl','oth'),
    'pid': lambda x: len(x)==9 and interval(x, 0, 999999999),
}

def passport_have_mandatory_fields(data):
    for field in MANDATORY_FIELDS.keys():
        if data.get(field, None)==None: return False
    return True

def passport_is_valid(data):
    for field, validator in MANDATORY_FIELDS.items():
        v = data.get(field, None)
        if v==None or not validator(v):
            return False
    return True

def scanner(lines):
    data = {}
    for line in lines:
        if len(line)==0:
            yield data
            data = {}
        else:
            for a,b in map(lambda x: x.split(':'), line.split(' ')):
                data[a]=b
    yield data

def do1(inputs):
    return sum(1 for _ in filter(passport_have_mandatory_fields, scanner(inputs)))

def do2(inputs):
    return sum(1 for _ in filter(passport_is_valid, scanner(inputs)))
