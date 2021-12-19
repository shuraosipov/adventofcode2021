from typing import Counter

def load_input():
    template = []
    rules = {}
    with open('solutions/day14_input.txt', 'r') as f:
        for n, line in enumerate(f):
            value = line.strip()
            if n == 0:
                template = value
            elif value:
                pair, element = value.split(" -> ")
                rules[pair] = element
    return (template,rules)

def get_pairs(template):
    pairs = Counter()
    for i in range(0, len(template) - 1, 1):
        pairs[template[i:i+2]] += 1
    return pairs

def count_chars(pairs, template, rules, steps=10):
    for _ in range(steps):
        new_pairs = Counter()
        char_count = Counter()
        for k,v in pairs.items():
            p1,p2 = f"{k[0]}{rules[k]}", f"{rules[k]}{k[1]}"
            new_pairs[p1] += v
            new_pairs[p2] += v
            char_count[k[0]] += v
            char_count[rules[k]] += v
        pairs = new_pairs

    char_count[template[-1]] += 1

    return max(char_count.values()) - min(char_count.values())

template, rules = load_input()
pairs = get_pairs(template)
part1 = count_chars(pairs, template, rules, steps=10)
part2 = count_chars(pairs, template, rules, steps=40)

print("Part One:", part1)
print("Part Two:", part2)







