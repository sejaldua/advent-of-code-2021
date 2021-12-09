from aocd.models import Puzzle
from utils import get_test_input, write_solution
import numpy as np

"""
Day 9: Smoke Basin
"""

puzzle = Puzzle(year=2021, day=9)

def parse_input(data):
    return np.array([list(map(int, list(line))) for line in data.splitlines()])

def compare_vals(val, adj_val):
    return True if val < adj_val else False
    
def coords_in_bounds(coords, bounds):
    return coords[0] in range(bounds[0]) and coords[1] in range(bounds[1])

def is_min_adjacent(heightmap, row, col):
    neighbors = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]
    comparison_bools = []
    for adj_coords in neighbors:
        if coords_in_bounds(adj_coords, heightmap.shape):
            comparison_bools.append(compare_vals(heightmap[row][col], heightmap[adj_coords[0]][adj_coords[1]]))
    return all(comparison_bools)

"""
Part A: 

"""

def part_a(test: bool = False) -> int:
    data = get_test_input('day09') if test else Puzzle(year=2021, day=9).input_data
    heightmap = parse_input(data)
    low_points = []
    for row in range(heightmap.shape[0]):
        for col in range(heightmap.shape[1]):
            if is_min_adjacent(heightmap, row, col):
                low_points.append(heightmap[row][col])
    risk_levels = list(map(lambda x: x + 1, low_points))
    return sum(risk_levels)

assert(part_a(test=True) == 15)
answer_a = part_a()
write_solution('day09', 'a', answer_a)
puzzle.answer_a = answer_a

"""
Part B: 
"""
