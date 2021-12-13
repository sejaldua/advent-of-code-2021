from aocd.models import Puzzle
from utils import get_test_input, write_solution
import numpy as np

"""
Day 13: Transparent Origami
"""

puzzle = Puzzle(year=2021, day=13)

def get_unfolded_dot_paper(lines: list) -> np.ndarray:
    """ Construct the unfolded dot paper given dot coordinates """
    
    coords = [tuple(map(int, line.split(','))) for line in lines if ',' in line]
    folds = [tuple(line.strip('fold along ').split('=')) for line in lines if 'fold along' in line]
    folds = list(map(lambda x: (x[0], int(x[1])), folds))
    x_vals = set([tup[0] for tup in coords])
    y_vals = set([tup[1] for tup in coords])
    grid = np.zeros(shape=(max(y_vals)+1, max(x_vals)+1))
    for j, i in coords:
        grid[i][j] = 1
    return grid, folds

def perform_fold(grid, axis, index):
    if axis == 'y':
        new_grid = grid[:index, :] + np.flipud(grid[index+1:, :])
    else:
        new_grid = grid[:, :index] + np.fliplr(grid[:, index+1:])
    return new_grid
    
def driver(test: bool=False, one_fold: bool=True) -> int:
    """ Driver which works for Part A and B, only arg to flip is flag"""
    
    data = get_test_input('day13').splitlines() if test else Puzzle(year=2021, day=13).input_data.splitlines()
    grid, folds = get_unfolded_dot_paper(data)
    for fold in folds:
        grid = perform_fold(grid, *fold)
        if one_fold:
            return np.sum(grid != 0)
    answer_str = "\n".join(["".join(list(map(lambda x: "#" if x > 0 else " ", line))) for line in grid.tolist()])
    return answer_str
    

"""
Part A:
Your goal is to find the number of distinct paths that start at start, 
end at end, and don't visit small caves more than once. There are two types of 
caves: big caves (written in uppercase, like A, which can be visited any 
number of times) and small caves (written in lowercase, like b).
How many paths through this cave system are there that visit small caves at most once?
"""

assert(driver(test=True) == 17)
answer_a = driver()
write_solution('day13', 'a', answer_a)
# puzzle.answer_a = answer_a

"""
Part B: 
Now big caves can be visited any number of times, a single small cave can 
be visited at most twice, and the remaining small caves can be visited at 
most once.
The caves named start and end can only be visited exactly once each: once 
you leave the start cave, you may not return to it, and once you reach the 
end cave, the path must end immediately.
Given these new rules, how many paths through this cave system are there?
"""

answer_b = driver(one_fold=False)
write_solution('day13', 'b', answer_b)
# CURRENTLY: manual answer entry via inspecting output
# TODO: implement OCR to go from symbols to capital letter recognition?