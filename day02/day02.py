from aocd import get_data
from aocd.models import Puzzle
from aocd import submit

"""
Day 2: Deep Dive
"""

puzzle = Puzzle(year=2021, day=2)
data = puzzle.input_data.splitlines()

"""
Part 1: 
- forward X increases the horizontal position by X units.
- down X increases the depth by X units.
- up X decreases the depth by X units.

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""
# naive solution
horiz, depth = 0, 0
for line in data:
    direction, units = line.split(' ')
    units = int(units)
    if direction == 'forward':
        horiz += units
    elif direction == 'down':
        depth += units
    elif direction == 'up':
        depth -= units
puzzle.answer_a = horiz * depth

"""
Part 2:
- down X increases your aim by X units.
- up X decreases your aim by X units.
- forward X does two things:
    - It increases your horizontal position by X units.
    - It increases your depth by your aim multiplied by X.

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""

