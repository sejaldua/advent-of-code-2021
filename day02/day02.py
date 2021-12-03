from aocd.models import Puzzle

"""
Day 2: Deep Dive
"""

"""
Part 1: 
- forward X increases the horizontal position by X units.
- down X increases the depth by X units.
- up X decreases the depth by X units.

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""

######### NAIVE SOLUTION #########
# horiz, depth = 0, 0
# for line in data:
#     direction, units = line.split(' ')
#     units = int(units)
#     if direction == 'forward':
#         horiz += units
#     elif direction == 'down':
#         depth += units
#     elif direction == 'up':
#         depth -= units
# puzzle.answer_a = horiz * depth

######### MORE ROBUST SOLUTION #########

# function to adjust position according to direction and number of units
def move(pos, direction, units):
    if direction == "forward":
        return (pos[0] + units, pos[1])
    elif direction == "down":
        return (pos[0], pos[1] + units)
    elif direction == "up":
        return (pos[0], pos[1] - units)
    raise ValueError

"""
Part 2:
- down X increases your aim by X units.
- up X decreases your aim by X units.
- forward X does two things:
    - It increases your horizontal position by X units.
    - It increases your depth by your aim multiplied by X.

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""

# function to adjust position and aim according to direction and number of units
def move_with_aim(pos, direction, units):
    if direction == "forward":
        return (pos[0] + units, pos[1] + (pos[2] * units), pos[2])
    elif direction == "down":
        return (pos[0], pos[1], pos[2] + units)
    elif direction == "up":
        return (pos[0], pos[1], pos[2] - units)
    raise ValueError

# puzzle.answer_b = pos[0] * pos[1]

#####################################################

# parse each line, splitting into a direction and number of units
def parse(line):
    direction, units = line.split(" ")
    return direction, int(units)

def driver(pos, helper_func):
    global commands
    for cmd in commands:
        pos = helper_func(pos, *cmd)
    # multiply final horizontal position by final depth position
    return pos[0] * pos[1]

puzzle = Puzzle(year=2021, day=2)
data = puzzle.input_data.splitlines()
commands = list(map(parse, data))
puzzle.answer_a = driver((0,0), move)
puzzle.answer_b = driver((0,0,0), move_with_aim)
