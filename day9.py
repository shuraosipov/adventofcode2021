import numpy as np

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column

        self.pos = (self.row, self.column)

# with open('day9_input.txt', 'r') as f:
#     data = [] 
#     for line in f:
#         ints = []
#         value = line.rstrip()
#         for char in value:
#             ints.append(int(char))
#         data.append(ints)

data = []
with open('day9_input.txt', 'r') as f:
    for line in f:
        value = [int(x) for x in list((line.strip()))]
        data.append(value)

def create_matrix(data):
    matrix = []
    for i in range(len(data)):
        x = np.array(data[i])
        matrix.append(x)
    return matrix

def get_next_cell(current, matrix):
    x = current.row
    y = current.column
    value = matrix[x][y]

    next_cell = current

    if x > 1 and value > matrix[x-1][y]:
        value =  matrix[x-1][y]
        next_cell = Cell(x-1,y)
    
    if y > 1 and value > matrix[x][y-1]:
        value = matrix[x][y-1]
        next_cell = Cell(x,y-1)
    
    if x < len(matrix) -1 and value > matrix[x+1][y]:
        value = matrix[x+1][y]
        next_cell = Cell(x+1,y)  

    if y < len(matrix[1]) -1 and value > matrix[x][y+1]:
        value = matrix[x][y+1]
        next_cell = Cell(x,y+1)
    
    return next_cell


def find_local_minimum(current, matrix):
    next_cell = get_next_cell(current, matrix)
    if next_cell == current:
        return current
    else:
        return find_local_minimum(next_cell, matrix)

M = create_matrix(data)
initial_position = Cell(0,0)

#print(data)

R = len(data)
C = len(data[0])

RR = {}
for r in range(R):
    for c in range(C):
        print(r,c)
        #print(data[r][c])
        cell = Cell(r,c)
        loc_min = find_local_minimum(cell, M)
        print(loc_min.pos)
        pos = loc_min.pos
        val = data[loc_min.row][loc_min.column]
        print(val)

        if pos not in RR:
            RR[pos] = val







