# An infinite number of shelves are arranged one above the other in a staggered fashion.
# The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 (the cat cannot climb on the shelf directly above its head), according to the illustration:

#                  ┌────────┐
#                  │-6------│
#                  └────────┘
# ┌────────┐       
# │------5-│        
# └────────┘  ┌─────► OK!
#             │    ┌────────┐
#             │    │-4------│
#             │    └────────┘
# ┌────────┐  │
# │------3-│  │     
# BANG!────┘  ├─────► OK! 
#   ▲  |\_/|  │    ┌────────┐
#   │ ("^-^)  │    │-2------│
#   │ )   (   │    └────────┘
# ┌─┴─┴───┴┬──┘
# │------1-│
# └────────┘
# Input
# Start and finish shelf numbers (always positive integers, finish no smaller than start)

# Task
# Find the minimum number of jumps to go from start to finish

# Example
# Start 1, finish 5, then answer is 2 (1 => 4 => 5 or 1 => 2 => 5)

def solution(start, stop):
    jumps = 0
    current_step = start
    while current_step +3 <= stop:
        current_step +=3
        jumps +1
    while current_step < stop:
        current_step +=1
        jumps +=1
    return jumps

def solution(start, end):
    total_steps = end - start
    three_step_jumps = total_steps //3
    one_step_jumps = total_steps %3
    return three_step_jumps 
def soln(start, stop):
    diff = stop-startres = diff // 3+ diff %3
    return res