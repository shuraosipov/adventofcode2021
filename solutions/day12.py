# just copied from here - https://www.youtube.com/watch?v=zjq2fGmz2Sg&ab_channel=JonathanPaulson

from collections import defaultdict, deque


E = defaultdict(list)
with open('solutions/day12_input.txt', 'r') as f:
    for line in f:
        a,b = line.strip().split("-")
        E[a].append(b)
        E[b].append(a)

print(E)
start = ('start', set(['start']), None)
ans = 0
Q = deque([start])
print(Q)

while Q:
    pos, small, twice = Q.popleft()
    #print(pos, small)
    if pos == 'end':
        ans += 1
        continue
    
    for y in E[pos]:
        if y not in small:
            new_small = set(small)
            if y.islower():
                new_small.add(y)
            Q.append((y,new_small, twice))
        elif y in small and twice is None and y not in ['start','end']:
            Q.append((y,small,y))

    
print(ans)