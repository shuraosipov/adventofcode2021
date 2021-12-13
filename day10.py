def remove_legit_chunks(s):
    for c in chunks:
        s = s.replace(c,"")
    if any(c in s for c in chunks):
        return remove_legit_chunks(s)
    return s

def find_illegal_character(line):
    new_line = [x for x in line]
    for i in range(len(new_line) -1):
        if new_line[i] in open_chars and new_line[i+1] in close_chars:
            if valid_pairs[new_line[i]] != new_line[i+1]:
                #print(f"{line} -Expected '{valid_pairs[new_line[i]]}', but found '{new_line[i+1]}' instead")
                illegal_character = new_line[i+1]
                return illegal_character

def check_if_complete(s):
    if any(c in s for c in close_chars):
        return True
    return False



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


lines = []
with open('day10_input.txt','r') as f:
    for line in f:
        lines.append(line.strip())

# Part One

ans = 0
for line in lines:
    new_line = remove_legit_chunks(line)
    if check_if_complete(new_line):
        illegal_char = find_illegal_character(new_line)
        print(illegal_char)
        ans += scores[illegal_char]

print(ans)