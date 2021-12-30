# Courtesy to - https://gist.github.com/joshbduncan/0286c34009e16f67f8e76d189983cd4d

import re
import math
import itertools

def load_data():
    with open('solutions/day18_input.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def add(line):
    if " + " in line:
        line = f"[{line.split(' + ')[0]},{line.split(' + ')[1]}]"
    return line

def explode(line):
    """
    To explode a pair:

    1) the pair's left value is added to the first regular number to the left of the exploding pair (if any), 
    2) the pair's right value is added to the first regular number to the right of the exploding pair (if any). 
    Exploding pairs will always consist of two regular numbers. 
    3) Then, the entire exploding pair is replaced with the regular number 0.

    """
    
    offset = 0
    pairs = re.findall("\[\d+,\d+\]", line)
    for p in pairs:
        pair = re.search(re.escape(p), line[offset:])
        left_brackets = line[:pair.start() + offset].count("[")
        right_brackets = line[:pair.start() + offset].count("]")

        if left_brackets - right_brackets >= 4:
            x,y = pair.group()[1:-1].split(",")
            left = line[:pair.start() + offset][::-1]
            right = line[pair.end() + offset:]
            
            search_left = re.search("\d+", left)
            if search_left:
                new_left_value = int(left[search_left.start():search_left.end()][::-1]) + int(x)
                left = f"{left[:search_left.start()]}{str(new_left_value)[::-1]}{left[search_left.end():]}"
            
            search_right = re.search("\d+", right)
            if search_right:
                new_right_value = int(right[search_right.start():search_right.end()]) + int(y)
                right = f"{right[:search_right.start()]}{new_right_value}{right[search_right.end():]}"
            line = f"{left[::-1]}0{right}"
            break
        else:
            offset = pair.end() + offset
    return line

def reduce(line):
    exploded = explode(line)
    if exploded != line:
        return reduce(exploded)
    else:
        splited = split(line)
        if splited != line:
            return reduce(splited)
        else:
            return splited

def split(line):
    GREATER_THAN_10 = re.search("\d\d", line)
    if GREATER_THAN_10:
        left = line[:GREATER_THAN_10.start()]
        right = line[GREATER_THAN_10.end():]
        left_digit = int(math.floor(int(GREATER_THAN_10.group()) / 2))
        right_digit = int(math.ceil(int(GREATER_THAN_10.group()) / 2))
        line = f"{left}[{left_digit},{right_digit}]{right}"
    return line


def magnitude(final_sum):
    while final_sum.count(",") > 1:
        #print(final_sum)
        for p in re.findall("\[\d+,\d+\]", final_sum):
            pair = re.search(re.escape(p), final_sum)
            left_digit, right_digit = p[1:-1].split(",")
            final_sum = f"{final_sum[: pair.start()]}{int(left_digit) * 3 + int(right_digit) * 2}{final_sum[pair.end() :]}"
    left_digit, right_digit = final_sum[1:-1].split(",")
    return int(left_digit) * 3 + int(right_digit) * 2

lines = load_data()

# Part One
final_sum = ""
while lines:
    line1 = lines.pop(0)
    if not final_sum:
        line2 = lines.pop(0)
        final_sum = f"{line1} + {line2}"
    else:
        final_sum = f"{final_sum} + {line1}"
    final_sum = reduce(add(final_sum))

print("Part One:",magnitude(final_sum))

# Part Two
lines2 = load_data()
magnitudes = set()
pairs = list(itertools.permutations(lines2, 2))
for pair in pairs:
    final_sum = reduce(add(f"{pair[0]} + {pair[1]}"))
    magnitudes.add(magnitude(final_sum))
print("Part Two:",max(magnitudes))
