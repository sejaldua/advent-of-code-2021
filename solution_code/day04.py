from aocd.models import Puzzle
from utils import get_test_input, write_solution
import numpy as np

"""
Day 4: Giant Squid
"""

puzzle = Puzzle(year=2021, day=4)

def parse_raw_data(data):
    draws, *boards = data.split('\n\n')
    draws = list(map(int, draws.split(',')))
    boards = [{
        'values': 
            [
                [int(cell) for cell in row.split(' ') if cell != '']
                for row in board.split('\n')
            ],
        'markers': 
            [
                [0 for i in range(5)] 
                for j in range(5)
            ]
        }
        for board in boards
    ]
    return draws, boards

"""
Part A: 
Each bit in the gamma rate can be determined by finding the MOST common bit in 
the corresponding position of all numbers in the diagnostic report.
Each bit in the epsilon rate can be determined by finding the LEAST common bit.
Use the binary numbers in your diagnostic report to calculate the gamma rate 
and epsilon rate, then multiply them together. What is the power consumption of 
the submarine?
"""

def get_board_dicts(boards):
    board_dicts = [
            {
                cell: (x, y)
                for x, row in enumerate(board['values'])
                for y, cell in enumerate(row)
            }
            for board in boards
        ]
    return board_dicts


def check_markers(arr):
    t_arr = [list(i) for i in zip(*arr)]
    if any(list(map(lambda x: True if sum(x) == len(arr) else False, arr))):
        return True
    elif any(list(map(lambda x: True if sum(x) == len(arr) else False, t_arr))):
        return True
    else:
        return False

def part_a(test=False):
    data = get_test_input('day04') if test else Puzzle(year=2021, day=4).input_data
    draws, boards = parse_raw_data(data)
    board_dicts = get_board_dicts(boards)
    for draw in draws:
        for i, board in enumerate(boards):
            try:
                row, col = board_dicts[i][draw]
                board['markers'][row][col] += 1
                if check_markers(board['markers']):
                    marked_vals = np.array(board['values']) * np.array(board['markers'])
                    unmarked_sum = np.sum(board['values']) - np.sum(marked_vals)
                    return unmarked_sum * draw
            except KeyError:
                continue
    
assert(part_a(test=True) == 4512)
answer_a = part_a()
write_solution('day04', 'a', answer_a)
puzzle.answer_a = answer_a