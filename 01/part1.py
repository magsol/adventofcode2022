import numpy as np

# Input: the number of Calories each elf is carrying

elves = [[]]
totals = []

with open("01_p1.txt", "r") as f:
    total = 0
    for line.strip() in f:
        if len(line) > 0:
            # Another calorie count for the current elf.

            c = int(line)
            total += c
            elves[-1].append(c)
        else:
            # A blank line. Joy.
            totals.append(total)
            total = 0
            elves.append([])

# Part 1: Find the Elf carrying the most Calories. 
# How many total Calories is that Elf carrying?
totals_numpy = np.array(totals)
elf_carrying_largest = totals_numpy.argmax()
largest_total = totals_numpy[elf_carrying_largest]
print(f"Highest carried calorie count is {largest_total}.")

# Part 2: Find the top three Elves carrying the most Calories. 
# How many Calories are those Elves carrying in total?
indices = totals_numpy.argsort()[::-1]
largest_three = totals_numpy[indices[:3]].sum()
print(f"Total calories carried by the three Elves carrying the most is {largest_three}.")
