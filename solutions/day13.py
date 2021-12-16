from collections import Counter
import numpy as np


xs = []
ys = []
coordinates = []

fold_instructions = [("y",7), ("x",5)]

with open('solutions/day13_input.txt', 'r') as f:
    for line in f:
        y,x = line.strip().split(",")
        xs.append(int(x))
        ys.append(int(y))
        
        coordinates.append((int(x),int(y)))


print (f"We have an array with {max(xs)} rows and {max(ys)} columns ")
for f in fold_instructions:
    print(f"Fold along {f[0]}={f[1]}")


# we need to divide an initial array
# get what's left on the bottom and fold it up
# 

def create_array(rows, cols, coordinates):
    A = np.zeros((rows + 1, cols + 1))
    for c in coordinates:
        x = c[0]
        y = c[1]
        A[x][y] = 1
    return A



def fold_horizontally(ary, line):
    top, bottom_temp = np.split(ary, [line], axis=0)
    bottom = np.delete(bottom_temp, 0, 0)
    
    return top + flip_up(bottom)

def flip_up(ary):
    return np.flip(ary, axis=0)

def fold_vertically(ary, line):
    left, right_temp = np.split(ary, [line], axis=1)
    right = np.delete(right_temp, 0, 1)
    return left + flip_left(right)

def flip_left(ary):
    return np.flip(ary, axis=1)

def count_visible_dots(ary):
    return np.count_nonzero(ary != 0)


A = create_array(max(xs), max(ys), coordinates)

c = fold_horizontally(A, 7)
print(c)
print(np.count_nonzero(c != 0))
