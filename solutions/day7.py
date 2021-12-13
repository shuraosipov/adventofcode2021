def load_input(file) -> list:
    with open(file, 'r') as f:
        line = f.readline()
        result = [int(x) for x in line.split(",")]
        return result
    
def get_fuel_burn_rate(steps):
    return int(steps * (steps + 1) / 2)

def part_one():
    Y = {}
    for pos in range(start, end):
        for i in input:
            if pos not in Y:
                Y[pos] = abs(i-pos)
            else:
                Y[pos] += abs(i-pos)

    return min(Y.values())


def part_two():
    Y = {}
    for pos in range(start, end):
        for i in input:
            burn_rate = get_fuel_burn_rate(abs(i-pos))
            
            if pos not in Y:
                Y[pos] = burn_rate
            else:
                Y[pos] += burn_rate

    return min(Y.values())


input = load_input('day7_input.txt')
start, end = min(input), max(input) + 1
print(part_one())
print(part_two())
    



        
    
    
        
        
