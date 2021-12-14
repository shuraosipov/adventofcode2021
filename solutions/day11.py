class Octopus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy_level = grid[x][y]
        self.adj_points = get_adj_points(x,y)

    def reset_energy_level(self):
        grid[self.x][self.y] = 0
    
    def increase_energy_level(self):
        grid[self.x][self.y] += 1

    def get_energy_level(self):
        return grid[self.x][self.y]

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

def flash(oct):
    global ans1
    ans1 += 1 
    oct.reset_energy_level()
    flushed.append((oct.x,oct.y))
    increase_adj_energy(oct)

def increase_adj_energy(oct):
    adj_points = get_adj_points(oct.x,oct.y)
    
    for points in adj_points:
        x,y  = points[0], points[1]
        oct = Octopus(x,y)
        if (oct.x,oct.y) not in flushed:
            oct.increase_energy_level()
        if oct.get_energy_level() > 9:
            flash(oct)

def all_zeros():
    if sum(sum(a) for a in grid) == 0:
        return True
    return False


def load_input():
    grid = []
    with open('solutions/day11_input.txt', 'r') as f:
        for line in f:
            grid.append([int(x) for x in line.strip()])
    return grid


if __name__ == '__main__':
    grid = load_input()

    ans1 = 0
    
    R = len(grid)
    C = len(grid[0])

    for step in range(1,500):
        flushed = []
        increase_grid_by_one()

        for r in range(R):
            for c in range(C):
                oct = Octopus(r,c)
                if oct.get_energy_level() > 9:
                    flash(oct)

        if all_zeros():
            ans2 = step
            break

    print('After step :', step)
    print_grid()
    print("Part One:",ans1)
    print("Part Two:",ans2)  