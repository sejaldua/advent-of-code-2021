from aocd.models import Puzzle

"""
Day 3: Binary Diagnostic
"""

"""
Part 1: 
Each bit in the gamma rate can be determined by finding the MOST common bit in 
the corresponding position of all numbers in the diagnostic report.
Each bit in the epsilon rate can be determined by finding the LEAST common bit.
Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine?
"""

puzzle = Puzzle(year=2021, day=3)
data = puzzle.input_data.splitlines()
int_array = list(map(lambda line: [int(char) for char in list(line)], data))
transposed = [list(i) for i in zip(*int_array)]
gamma_bits = list(map(lambda bits: '0' if sum(bits) < len(bits) // 2 else '1', transposed))
epsilon_bits = list(map(lambda x: '0' if x == '1' else '1', gamma_bits))
gamma_rate = int("".join(gamma_bits), 2)
epsilon_rate = int("".join(epsilon_bits), 2)    
puzzle.answer_a = gamma_rate * epsilon_rate

"""
Part 2:
"""
