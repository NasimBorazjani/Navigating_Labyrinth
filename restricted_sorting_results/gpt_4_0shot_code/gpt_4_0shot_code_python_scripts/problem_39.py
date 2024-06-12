
from collections import deque
from itertools import combinations
from copy import deepcopy

# Define the initial state of the stacks
stacks = [['Green', 'Green', 'Black', 'Blue', 'Black'], [], [], [], ['Yellow', 'Red', 'Black', 'Red', 'Blue'], ['Yellow', 'Blue', 'Red', 'Black', 'Blue'], ['Red', 'Green', 'Green', 'Yellow', 'Yellow'], []]
# Define the cost of moving a block to each stack
costs = {0: 8, 1: 8, 2: 1, 3: 2, 4: 9, 5: 4, 6: 7, 7: 8}

# Define the goal state
goal = [['Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], []]

# Define a function to check if a move is valid
def valid_move(stacks, from_stack, to_stack):
    if not stacks[from_stack]:
        return False
    if not stacks[to_stack]:
        return True
    if stacks[from_stack][-1] == stacks[to_stack][-1]:
        return True
    return False

# Define a function to perform a move
def do_move(stacks, from_stack, to_stack):
    block = stacks[from_stack].pop()
    stacks[to_stack].append(block)
    return stacks

# Define a function to find the minimum cost solution
def find_min_cost(stacks, costs, goal):
    queue = deque([(stacks, [], 0)])
    min_cost = float('inf')
    min_solution = None
    while queue:
        stacks, solution, cost = queue.popleft()
        if stacks == goal:
            if cost < min_cost:
                min_cost = cost
                min_solution = solution
        else:
            for from_stack, to_stack in combinations(range(8), 2):
                if valid_move(stacks, from_stack, to_stack):
                    new_stacks = deepcopy(stacks)
                    new_stacks = do_move(new_stacks, from_stack, to_stack)
                    new_solution = solution + [(from_stack, to_stack)]
                    new_cost = cost + costs[to_stack]
                    queue.append((new_stacks, new_solution, new_cost))
    return min_solution

# Find the minimum cost solution
solution = find_min_cost(stacks, costs, goal)
print(solution)
