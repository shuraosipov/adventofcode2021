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


def count_target_hits(Xs,Ys):
    x1,x2,y1,y2 = Xs[0],Xs[1],Ys[0],Ys[1]   

    max_y = 0
    target_hits = 0
    for y in range(y1, abs(y1)):
        for x in range(1,x2+1):
            vx,vy = x,y
            x_p = y_p = 0
            max_y_path = 0
            
            for _ in range(2 * abs(y1) + 2):
                x_p += vx
                y_p += vy
                vx = max(vx-1, 0)
                vy -= 1
                max_y_path = max(max_y_path, y_p)


                if x1 <= x_p <= x2 and y1 <= y_p <= y2:
                    max_y = max(max_y_path, max_y)
                    target_hits += 1
                    break
                elif x_p > x2 or y_p < y1:
                    break
    
    return target_hits


Xs, Ys = load_input()
print("Part One:",max_Y(Ys))
print("Part Two:",count_target_hits(Xs,Ys))



