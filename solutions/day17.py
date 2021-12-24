# On each step, these changes occur in the following order:

# The probe's x position increases by its x velocity.
# The probe's y position increases by its y velocity.
# Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
# Due to gravity, the probe's y velocity decreases by 1.

start = (0,0)

# The probe launcher on your submarine can fire the probe with any integer velocity in the x (forward)
# and y (upward, or downward if negative)

# target area: x=20..30, y=-10..-5

x_pos, y_pos = 0,0
x_vel, y_vel = 6,9 # we need to find this!
target_x1, target_x2 = 20,30
target_y1, target_y2 = -10,-5

ans = 0
max_y_pos = 0
while not target_x1 <= x_pos <= target_x2  or not target_y1 <= y_pos <= target_y2:
    # print(x_vel, y_vel)
    # print(x_pos, y_pos)
    
    # The probe's x position increases by its x velocity.
    x_pos += x_vel
    # The probe's y position increases by its y velocity.
    y_pos += y_vel
    
    # Due to drag, the probe's x velocity changes by 1 toward the value 0; 
    # It decreases by 1 if it is greater than 0
    if x_vel > 0:
        x_vel -= 1
    # It increases by 1 if it is less than 0, or does not change if it is already 0.    
    elif x_vel < 0:
        x_vel += 1

    # Due to gravity, the probe's y velocity decreases by 1.
    y_vel -= 1

    print("Coordinates",x_pos, y_pos)
    print("Velocity",x_vel, y_vel)
    ans += 1
    
    if y_pos > max_y_pos:
        max_y_pos = y_pos

print(ans)
print(max_y_pos)

## pseudo code
# find velocity knowing target area (20,30),(-10,-5) and launch location (0,0)




