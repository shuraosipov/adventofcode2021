# Calculate the horizontal position and depth you would have after following the planned course.

with open('day2_input.txt', 'r') as f:
    instructions = []
    for value in f:
        instructions.append(value.split())


def calculate_location(instructions):
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in instructions:
        action = command[0]
        steps = int(command[1])

        if action == 'forward':
            horizontal_position += steps
            depth += aim * steps
        elif action == 'down':
            aim += steps
        elif action == 'up':
            aim -= steps
    
    return (horizontal_position, depth)

horizontal_position, depth = calculate_location(instructions)

print(f"After following all instructions, we have a horizontal position of {horizontal_position} and a depth of {depth}.")
print("Number we get after multipling our final horizontal position by your final depth is", horizontal_position * depth)
    

