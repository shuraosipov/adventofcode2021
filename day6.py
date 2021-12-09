
# 
def load_input(file) -> list:
    with open(file, 'r') as f:
        line = f.readline()
        result = [int(x) for x in line.split(",")]
        return result



def calculate_reproduction(fish_list):
    
    new_fishes = []
        
    for id, timer in enumerate(fish_list):
        if timer == 0:
            timer = 6
            fish_list[id] = timer
            new_fishes.append(1)
        else:
            timer -= 1
            fish_list[id] = timer
        
    if len(new_fishes) > 0:
        for _ in range(len(new_fishes)):
            fish_list.append(8)
    
    print(f"After {day} days: {len(fish_list)} fish")


fish_list = load_input('day6_input.txt')
days = 80

for day in range(days + 1):
    if day == 0:
        print("Initial state:", len(fish_list), "fish")
    else:
        calculate_reproduction(fish_list)
    
print(f"After {days} days, there are a total of {len(fish_list)} fish")