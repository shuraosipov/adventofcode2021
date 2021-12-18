#import numpy as np
# Inititally, I've tried to solve this puzzle with numpy.
# The basic idea is to get the array, split it (get two left,right or up, down). 
# Flip right, or down array and add them to the left, up side. 
# While it works on the sample data, I was not able to make it work on the test data.
# numpy code here is just for reference


xs = []
ys = []
coordinates = set()
fold_instructions = []

with open('solutions/day13_input.txt', 'r') as f:
    for line in f:
        new_line = line.strip()
        if len(new_line) > 0:
            if 'fold' in new_line:
                i = new_line.split()[-1].split("=")
                fold_instructions.append([i[0],int(i[1])])
            else:
                x,y = new_line.split(",")
                xs.append(int(x))
                ys.append(int(y))
        
            coordinates.add((int(x),int(y)))

# def create_array(rows, cols, coordinates):
#     A = np.zeros((rows + 1, cols + 1))
#     for c in coordinates:
#         x = c[0]
#         y = c[1]
#         A[x][y] = 1
#     return A

# def fold_horizontally(ary, line):
#     top, bottom_temp = np.split(ary, [line], axis=0)
#     bottom = np.delete(bottom_temp, 0, 0)
    
#     return top + flip_up(bottom)

# def flip_up(ary):
#     return np.flip(ary, axis=0)

# def fold_vertically(ary, line):
#     left, right_temp = np.split(ary, [line], axis=1)
#     right = np.delete(right_temp, 0, 1)
#     return left + flip_left(right)

# def flip_left(ary):
#     return np.flip(ary, axis=1)

# def count_visible_dots(ary):
#     return np.count_nonzero(ary)


# def fold(ary, pos):
#     new_array = ary
#     if pos[0] == 'y':
#         new_array = fold_horizontally(new_array, pos[1])
#     elif pos[0] == 'x':
#         new_array = fold_vertically(new_array, pos[1])
#     return new_array

def print_coord(coords):
    max_x = max(x for x,_ in coords)
    max_y = max(y for _,y in coords)

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if (x,y) in coords:
                print('◼', end='')
            else:
                print(' ', end='')
        print()
       
def fold_paper(coordinates, instructions, first_only=True):
    for f in instructions:
        axis, line = f
        if axis == 'y':
            for x,y in coordinates.copy():
                if y > line:
                    coordinates.remove((x,y))                
                    coordinates.add((x,2*line - y))
                elif y < line:
                    coordinates.add((x,y))
        elif axis == 'x':
            for x,y in coordinates.copy():
                if x > line:  
                    coordinates.remove((x,y))                  
                    coordinates.add((2*line - x,y))
                elif x < line:
                    coordinates.add((x,y))
        if first_only:
            break

    return coordinates

answer1 = fold_paper(coordinates, fold_instructions)
print("Part One:",len(answer1))
#print_coord(answer)

answer2 = fold_paper(coordinates, fold_instructions, first_only=False)
print("Part Two:")
print_coord(answer2)

