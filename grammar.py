import random

def make_grammar(filename):
    text = open(filename)
    lines = text.read().splitlines()
    ret = []
    for x in range(0, len(lines)):
        ret.append(lines[x].split('::=')[0])
        ret.append(lines[x].split('::=')[1].split('|'))
    return {ret[x] : ret[x+1] for x in range(0, len(ret), 2)}

def generate(dictionary, tok):
    if tok not in dictionary:
        return tok
    else:
        rules = dictionary[tok]
        alt = rules[random.randint(0, len(rules) - 1)]
        toks = alt.split()
        return "".join([generate(dictionary, tok) for tok in toks])


def get_input():
        start = raw_input('Enter starting file name: ')
        make_grammar(start)


print make_grammar('numbers.txt')
print generate(make_grammar('numbers.txt'), 'exp')