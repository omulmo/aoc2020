

def count_trees(forest, dx, dy):
    n = 0
    col = 0
    for row in range(0, len(forest), dy):
        trees = forest[row]
        if trees[col]=='#' : n+=1
        col = (col+dx) % len(trees)
    return n

def do1(inputs):
    return count_trees(inputs, 3, 1)

def do2(inputs):
    n = 1
    for dx, dy in (1,1), (3,1), (5,1), (7,1), (1,2):
        n *= count_trees(inputs, dx, dy)
    return n
