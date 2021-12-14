from collections import deque

grid = []
with open('solutions/day11_input.txt', 'r') as f:
    for line in f:
        # print(line.strip())
        new_line = [int(x) for x in line.strip()]
        grid.append(new_line)


def get_adj_points(x, y):
    adj_points = []
    if x > 0:
        adj_points.append((x - 1, y)) # row above
    if x < R - 1:
        adj_points.append((x + 1, y)) # row below
    if y > 0:
        adj_points.append((x, y - 1)) # column left
    if y < C - 1:
        adj_points.append((x, y + 1)) # column right

    # If we a not on the borders or edges
    # Append diagonal coordinates
    if x > 0 and y > 0 and x < R - 1 and y < C - 1:
        adj_points.append((x - 1, y - 1)) # up left
        adj_points.append((x - 1, y + 1)) # up right
        adj_points.append((x + 1, y - 1)) # down left
        adj_points.append((x + 1, y + 1)) # down right
    
    # we are on the top border
    if x == 0 and y != C-1 and y != 0:
        adj_points.append((x + 1, y - 1)) # down left
        adj_points.append((x + 1, y + 1)) # down right
    
    # we are on the left border
    if y == 0 and x != R-1 and x != 0:
        adj_points.append((x - 1, y + 1)) # up right
        adj_points.append((x + 1, y + 1)) # down right

    # we are on the bottom border
    if x == R -1 and y != C-1 and y != 0:
        adj_points.append((x - 1, y - 1)) # up left
        adj_points.append((x - 1, y + 1)) # up right
    
    # we are on the right border
    if y == C-1 and x != R-1 and x != 0:
        adj_points.append((x - 1, y - 1)) # up left
        adj_points.append((x + 1, y - 1)) # down left
    
    # we are on the top left edge
    if x == 0 and y == 0:
        adj_points.append((x + 1, y + 1)) # down right
    
    # we are on the top right edge
    if x == 0 and y == C-1:
        adj_points.append((x + 1, y - 1)) # down left
    
    # we are on the bottom left edge
    if x == R -1 and y == 0:
        adj_points.append((x - 1, y + 1)) # up right
    
    # we are on the bottom right edge
    if x == R -1 and y == C -1 :
        adj_points.append((x - 1, y - 1)) # up left

    return adj_points

def print_grid():
    for i in grid:
     print(i)
    print("\n")

def increase_grid_by_one():
    for id, i in enumerate(grid):
        grid[id] = [x+1 for x in i]


            

    


R = len(grid)
C = len(grid[0])

print(R, C)

print("Before any steps:")
print_grid()

class Octopus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy_level = grid[x][y]
        self.flashed = False
        self.adj_points = get_adj_points(x,y)

    def reset_energy_level(self):
        grid[self.x][self.y] = 0
    
    def increase_energy_level(self):
        grid[self.x][self.y] += 1

    def get_energy_level(self):
        return grid[self.x][self.y]

def increase_adj_energy(adj):
    
    for points in adj:
        x,y  = points[0], points[1]
        oct = Octopus(x,y)
        if (oct.x,oct.y) not in flushed:
            oct.increase_energy_level()
        if oct.get_energy_level() > 9:
            adj_to_flash.append(oct)
        
        print_grid()
        print("Adjacent to flash",adj_to_flash)
    

def flash(oct):
    oct.reset_energy_level()
    flushed.append((oct.x,oct.y))

    print_grid()

    adj_points = get_adj_points(oct.x,oct.y)
    increase_adj_energy(adj_points)

    #print(adj_to_flash)
    if len(adj_to_flash) > 0:
        return flash(adj_to_flash.pop())
   

    #return True

for step in range(1,3):
    print("Increased by one")
    increase_grid_by_one()
    print_grid()
    
    flushed = []
    adj_to_flash = deque()
    
    for r in range(R):
        for c in range(C):
            oct = Octopus(r,c)
            print(oct.energy_level, (oct.x, oct.y), oct.adj_points)
            if oct.get_energy_level() > 9:
                flash(oct)
            
            

    print('After step :', step)
    print_grid()
    