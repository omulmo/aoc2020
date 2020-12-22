from functools import reduce
from collections import defaultdict

def parse(inputs):
    sets = defaultdict(lambda: [])
    all_ingredients = defaultdict(lambda: 0)
    for line in inputs:
        lhs, rhs = line.split('(contains ')
        recipe = lhs.strip().split(' ')
        for ingredient in recipe:
            all_ingredients[ingredient] += 1
        for allergen in rhs.replace(')','').strip().split(', '):
            sets[allergen].append( set(recipe) )

    allergenes = {}
    for allergen, sets_of_ingredients in sets.items():
        allergenes[allergen] = reduce(lambda a,b: a & b, sets_of_ingredients)

    return all_ingredients, allergenes

def simplify(allergenes):
    queue=list(allergenes.keys())
    while len(queue)>0:
        allergen = queue.pop(0)
        ingredients = allergenes[allergen]
        if len(ingredients)==1:
            ingredient = list(ingredients)[0]
            for (k,v) in allergenes.items():
                if k==allergen: continue
                if ingredient in v:
                    v -= {ingredient}
                    queue.append(k)

    return allergenes


def do1(inputs):
    all_ingredients, allergenes = parse(inputs)
    allergenes = simplify(allergenes)
    remains = set(all_ingredients.keys()) - reduce(lambda a,b: a|b, allergenes.values())

    return sum(map(lambda x:all_ingredients[x], remains))

def do2(inputs):
    all_ingredients, allergenes = parse(inputs)
    allergenes = simplify(allergenes)
    return ','.join([ allergenes[key].pop() for key in sorted(allergenes.keys()) ])
