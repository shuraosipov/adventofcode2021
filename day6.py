
from types import resolve_bases


def load_input(file) -> list:
    with open(file, 'r') as f:
        line = f.readline()
        result = [int(x) for x in line.split(",")]
        return result


fish_list = load_input('day6_input.txt')
days = 80

for day in range(days + 1):
    if day == 0:
        print("Initial state:", len(fish_list), "fish")
    else:
        
        results = []
        for f in fish_list:
            if f == 0:
                results.append(6)
                results.append(8)
            else:
                results.append(f-1)
        fish_list = results
        print(f"After {day} days: {len(results)} fish")
    
print(f"After {days} days, there are a total of {len(fish_list)} fish")