chunks = ["[]","{}","()","<>"]
open_chars = ['(','[','{','<']
close_chars = [')',']','}','>']

valid_pairs = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

autocomplete_scores = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}

def remove_legit_chunks(line):
    for c in chunks:
        line = line.replace(c,"")
    if any(c in line for c in chunks):
        return remove_legit_chunks(line)
    return line

def find_illegal_character(line):
    new_line = [x for x in line]
    for i in range(len(new_line) -1):
        if new_line[i] in open_chars and new_line[i+1] in close_chars:
            if valid_pairs[new_line[i]] != new_line[i+1]:
                #print(f"{line} -Expected '{valid_pairs[new_line[i]]}', but found '{new_line[i+1]}' instead")
                illegal_character = new_line[i+1]
                return illegal_character

def is_compelete(line):
    if any(c in line for c in close_chars):
        return True
    return False

def find_closing_chars(line):
    closing_chars = []
    for c in line[::-1]:
        closing_chars.append(valid_pairs[c])
    return closing_chars

def calcualte_score(chars):
    score = 0
    for c in chars:
        score *= 5
        score += autocomplete_scores[c]
    return score


lines = []
with open('day10_input.txt','r') as f:
    for line in f:
        lines.append(line.strip())

ans1 = 0
ans2 = []

for line in lines:
    new_line = remove_legit_chunks(line)

    # Part One
    if is_compelete(new_line):
        illegal_char = find_illegal_character(new_line)
        ans1 += scores[illegal_char]
    
    # Part Two
    if not is_compelete(new_line):
        closing_chars = find_closing_chars(new_line)
        score = calcualte_score(closing_chars)
        ans2.append(score)

print("Part One", ans1)
print("Part Two", sorted(ans2)[len(ans2)//2])
