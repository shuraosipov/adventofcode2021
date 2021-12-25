import math

def load_input():
    with open('solutions/day17_input.txt', 'r') as f:
        _,_,Xs,Ys = f.readline().split()
        Xs = Xs[2:-1].split("..")
        Ys = Ys[2:].split("..")
        return (int(Xs[0]),int(Xs[1])),(int(Ys[0]),int(Ys[1]))

def max_Y(Ys):
    y1, _ = Ys[0], Ys[1]
    y0 = abs(y1) - 1
    return y0 * y0 - (y0 - 1) * y0 // 2
   
Xs, Ys = load_input()

print("Part One:",max_Y(Ys))

