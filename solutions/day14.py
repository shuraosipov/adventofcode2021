from collections import deque
from functools import wraps
from time import time

def get_pairs(template):
    return zip(template[1:], template)

def load_input():
    template = []
    rules = {}
    with open('solutions/day14_input.txt', 'r') as f:
        for n, line in enumerate(f):
            value = line.strip()
            if value and n == 0:
                template = value
            elif value:
                pair, element = value.split("->")
                rules[pair.strip()] = element.strip()
    
    return (template,rules)




def generate_template(pairs, rules):
    answer = []
    for p in pairs:
        r = f"{p[0]}{p[1]}"
        start, mid, end = p[0], rules[r], p[1]
        
        if len(answer) > 2:
            #answer[-1] = start
            answer.pop()
            answer.extend([start,mid,end])
            # answer.append(mid)
            # answer.append(end)
        else:
            # answer.append(start)
            # answer.append(mid)
            # answer.append(end)
            answer.extend([start,mid,end])
            
    return "".join(answer)


def generate_polymer(template, pairs, steps=10):
    #print("Template:     ",template)
    for i in range(1,steps+1):
        print(f"Step {i}:")
        ts = time()
        pairs = get_pairs(template)
        te = time()
        print(te-ts)
        ts = time()
        template = generate_template(pairs, rules)
        te = time()
        print(te-ts)
        print(len(template))

    print(f"Polymer length after {steps} steps is {len(template)}")
    return template

def get_answer(template):
    result = {}
    for i in set(template):
        #print(i, template.count(i))
        result[i] = template.count(i)

    max_ = max(result.values())
    min_ = min(result.values())

    return max_ - min_


template, rules = load_input()
pairs = get_pairs(template)
polymer = generate_polymer(template, pairs, steps=20)
print(get_answer(polymer))












    
