
from collections import deque
from copy import deepcopy

# Cost of moving a block to each stack
cost = {0: 3, 1: 6, 2: 3, 3: 6, 4: 9, 5: 6, 6: 6, 7: 10, 8: 2, 9: 5}

# Initial state of the stacks
stacks = [[], ['Yellow', 'White', 'Blue', 'Yellow', 'Red', 'White'], [], [], ['Blue', 'Blue', 'Green', 'Black', 'Black', 'Red'], ['Black', 'Green', 'Yellow', 'Yellow', 'Blue', 'Black'], [], ['White', 'Blue', 'Green', 'White', 'Yellow', 'Red'], [], ['Green', 'White', 'Black', 'Red', 'Green', 'Red']]

# Function to check if the blocks are sorted correctly
def is_sorted(stacks):
    for stack in stacks:
        if len(set(stack)) > 1:
            return False
    return True

# Function to generate all possible moves from the current state
def generate_moves(stacks):
    moves = []
    for i in range(len(stacks)):
        if stacks[i]:
            for j in range(len(stacks)):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]) and len(stacks[j]) < 6:
                    moves.append((i, j))
    return moves

# BFS algorithm to find the sequence of moves with the least cost
def bfs(stacks):
    queue = deque([(stacks, [], 0)])
    while queue:
        stacks, path, total_cost = queue.popleft()
        if is_sorted(stacks):
            return path
        for move in generate_moves(stacks):
            new_stacks = deepcopy(stacks)
            block = new_stacks[move[0]].pop()
            new_stacks[move[1]].append(block)
            new_path = path + [move]
            new_cost = total_cost + cost[move[1]]
            queue.append((new_stacks, new_path, new_cost))
    return []

print(bfs(stacks))
