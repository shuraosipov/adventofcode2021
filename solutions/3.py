complete = '[[<[([]))<([[{}[[()]]]'
incomplete = '<{([{{}}[<[[[<>{}]]]>[]]'
chunks = ["[]","{}","()","<>"]
close_chars = [')',']','}','>']

valid_pairs = {
    '(':')',
    '[':']',
    '{':'}',
    '<':'>'
}

autocomplete_scores = {
    ')':1,
    ']':2,
    '}':3,
    '>':4
}



def remove_legit_chunks(s):
    for c in chunks:
        s = s.replace(c,"")
    if any(c in s for c in chunks):
        return remove_legit_chunks(s)
    return s

def check_if_complete(s):
    # Return True is line is incomplete
    if any(c in s for c in close_chars):
        return True
    return False

def find_closing_chars(s):
    closing_chars = []
    for c in s[::-1]:
        closing_chars.append(valid_pairs[c])
    return closing_chars

def calcualte_score(chars):
    score = 0
    for c in chars:
        score *= 5
        score += autocomplete_scores[c]
    return score



s = remove_legit_chunks(incomplete)
print(s)
closing_chars = find_closing_chars(s)
print(closing_chars)
score = calcualte_score(closing_chars)
print(score)
