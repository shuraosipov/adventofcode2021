from collections import defaultdict, Counter

def load_input(file) -> list:
    with open(file, 'r') as f:
        line = f.readline()
        result = [int(x) for x in line.split(",")]
        return result

fish_map = Counter(load_input('day6_input.txt'))
#print(fish_map)

def calculate_lanternfish_reproduction(fish_map,days=80):
    for _ in range(days):
        temp = defaultdict(int)
        for f,count in fish_map.items():
            if f==0:
                temp[6] += count
                temp[8] += count
            else:
                temp[f-1] += count
            fish_map = temp
    return sum(fish_map.values())

print(calculate_lanternfish_reproduction(fish_map, days=80))
print(calculate_lanternfish_reproduction(fish_map, days=256))