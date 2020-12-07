

def parse(inputs):
    bags = {}
    for line in inputs:
        a,b = line.split('contain')
        bag_color = line.split('bags')[0].strip()
        content = []
        for item in b.split(','):
            words = item.strip().split(' ')
            if words[0]=='no':
                continue
            n = int(words[0])
            color = ' '.join(words[1:3])
            content.append( (n,color) )
        bags[bag_color] = content
    return bags

def has_color(bags, color_to_test, cache={}):
    if color_to_test not in cache:
        hasit=False
        for (n,color) in bags[color_to_test]:
            hasit = cache[color] if color in cache else color=='shiny gold' or has_color(bags, color, cache)
            if hasit: break
        cache[color_to_test] = hasit
    return cache[color_to_test]

def process(bags):
    cache={}
    for color in bags.keys():
        cache[color] = has_color(bags, color, cache)
    return cache

def n_of_bags(bags, color_of_bag, cache={}):
    sum = 1
    for (n,color) in bags[color_of_bag]:
        sum += n * (cache[color] if color in cache else n_of_bags(bags,color,cache))
    cache[color_of_bag] = sum
    return sum

def do1(inputs):
    bags = parse(inputs)
    return sum( 1 for _ in filter(lambda x:x, process(bags).values()))

def do2(inputs):
    bags = parse(inputs)
    return n_of_bags(bags, 'shiny gold')-1
