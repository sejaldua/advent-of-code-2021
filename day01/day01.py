from aocd import get_data
from aocd.models import Puzzle
from aocd import submit

"""
Day 1: Sonar Sweep
"""

"""
Part 1: 
How many measurements are larger than the previous measurement?
"""
puzzle = Puzzle(year=2021, day=1)
data = puzzle.input_data
nums = [int(n) for n in data.splitlines()]
answer_a = sum([1 if nums[i] > nums[i-1] else 0 for i in range(1, len(nums))])
# puzzle.answer_a = answer_a