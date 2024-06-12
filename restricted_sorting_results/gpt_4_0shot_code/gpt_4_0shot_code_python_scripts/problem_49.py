
from collections import deque
from copy import deepcopy

# Define the initial state of the stacks
stacks = [['Black', 'Green', 'Red', 'Yellow', 'Black'], [], ['Blue', 'Red', 'Black', 'Black', 'Yellow'], ['Green', 'Red', 'Yellow', 'Blue', 'Green'], [], [], ['Green', 'Blue', 'Red', 'Yellow', 'Blue'], []]

# Define the cost of moving one block to the top of each stack
costs = {0: 4, 1: 4, 2: 1, 3: 9, 4: 7, 5: 8, 6: 9, 7: 7}

# Define a function to check if a move is valid
def valid_move(from_stack, to_stack):
    if not stacks[from_stack]:
        return False
    if not stacks[to_stack]:
        return True
    if stacks[from_stack][-1] == stacks[to_stack][-1] and len(stacks[to_stack]) < 5:
        return True
    return False

# Define a function to check if the stacks are sorted
def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

# Define a function to find the move with the least cost
def find_least_cost_move():
    least_cost = float('inf')
    least_cost_move = None
    for from_stack in range(8):
        for to_stack in range(8):
            if valid_move(from_stack, to_stack):
                cost = costs[to_stack]
                if cost < least_cost:
                    least_cost = cost
                    least_cost_move = (from_stack, to_stack)
    return least_cost_move

# Define a function to perform a move
def perform_move(move):
    from_stack, to_stack = move
    block = stacks[from_stack].pop()
    stacks[to_stack].append(block)

# Define a function to solve the problem
def solve():
    moves = []
    while not is_sorted(stacks):
        move = find_least_cost_move()
        perform_move(move)
        moves.append(move)
    return moves

# Print the solution
print(solve())
