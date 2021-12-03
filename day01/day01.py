from aocd import get_data
from aocd.models import Puzzle
from aocd import submit

"""
Day 1: Sonar Sweep
"""

puzzle = Puzzle(year=2021, day=1)
data = puzzle.input_data
nums = [int(n) for n in data.splitlines()]

"""
Part 1: 
Count the number of times a depth measurement increases from the previous measurement. How many measurements are larger than the previous measurement?

    199 (N/A - no previous measurement)
    200 (increased)
    208 (increased)
    210 (increased)
    200 (decreased)
    207 (increased)
    240 (increased)
    269 (increased)
    260 (decreased)
    263 (increased)
"""

# iterate through each pair of adjacent nums
# check if rightmost num is greater than leftmost num
# sum how many times the check was true
answer_a = sum([1 if nums[i] > nums[i-1] else 0 for i in range(1, len(nums))])
# puzzle.answer_a = answer_a

"""
Part 2:
Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H
"""

# iterate through each sliding window of 3 adjacent digits
# count how many times rightmost sum was greater than leftmost sum
answer_b = sum([1 if sum(nums[i:i+3]) > sum(nums[i-1:i+2]) else 0 for i in range(1, len(nums)-2)])
# puzzle.answer_b = answer_b