result = {}

def update_results(point):
    if point not in result:
        result[point] = 0
    result[point] += 1

def calculate_vertical_lines(x1,x2,y1):
    for i in range(min(x1,x2),max(x1,x2) + 1):
        update_results((i,y1))

def calculate_horisontal_lines(x1, y1, y2):
    for i in range(min(y1,y2),max(y1,y2) + 1):
        update_results((x1,i))

def calculate_diagonal_lines(x1,x2,y1,y2):
    dx = x2 - x1
    dy = y2 - y1
    
    for i in range(1 + max(abs(dx),(dy))):
        
        m = 1 if dx > 0 else -1 if dx < 0 else 0
        x = x1 + m * i

        n = 1 if dy > 0 else -1 if dy < 0 else 0
        y = y1 + n * i

        update_results((x,y))

with open('day5_input.txt', 'r') as f:
    for line in f:
        start, end = line.split(" -> ")
        x1,y1 = start.split(",")
        x2,y2 = end.split(",")

        x1 = int(x1.strip())
        y1 = int(y1.strip())
        x2 = int(x2.strip())
        y2 = int(y2.strip())

        if x1 == x2:
           calculate_horisontal_lines(x1, y1, y2)
        elif y1 == y2:
            calculate_vertical_lines(x1,x2,y1)
        else:
            calculate_diagonal_lines(x1,x2,y1,y2)

# How many points do at least two lines overlap?
print(sum(value >= 2  for value in result.values()))
            

        



