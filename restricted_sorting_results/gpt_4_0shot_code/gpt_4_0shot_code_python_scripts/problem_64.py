
import copy

# Define the initial state of the stacks and the cost of moving a block to each stack
stacks = [['White', 'White', 'Yellow', 'White', 'White', 'Black'], [], ['Red', 'Red', 'Green', 'Green', 'Green', 'Red'], ['Black', 'Yellow', 'Black', 'Yellow', 'Blue', 'Green'], ['Yellow', 'Blue', 'Black', 'Green', 'Blue', 'Red'], [], ['Red', 'Black', 'Blue', 'Yellow', 'Blue', 'White'], [], [], []]
costs = {0: 6, 1: 7, 2: 11, 3: 10, 4: 7, 5: 2, 6: 3, 7: 3, 8: 11, 9: 8}

# Define a function to check if a move is valid
def is_valid_move(stacks, src, dest):
    return stacks[src] and (not stacks[dest] or stacks[dest][-1] == stacks[src][-1]) and len(stacks[dest]) < 6

# Define a function to perform a move
def make_move(stacks, src, dest):
    stacks = copy.deepcopy(stacks)
    stacks[dest].append(stacks[src].pop())
    return stacks

# Define a function to check if the goal state has been reached
def is_goal_state(stacks):
    for stack in stacks:
        if stack and len(set(stack)) > 1:
            return False
    return True

# Implement the DFS algorithm with backtracking
def dfs(stacks, cost, moves):
    if is_goal_state(stacks):
        return cost, moves
    min_cost = float('inf')
    min_moves = None
    for src in range(10):
        for dest in range(10):
            if src != dest and is_valid_move(stacks, src, dest):
                new_stacks = make_move(stacks, src, dest)
                new_cost = cost + costs[dest]
                new_moves = moves + [(src, dest)]
                temp_cost, temp_moves = dfs(new_stacks, new_cost, new_moves)
                if temp_cost < min_cost:
                    min_cost = temp_cost
                    min_moves = temp_moves
    return min_cost, min_moves

# Run the DFS algorithm from the initial state
min_cost, min_moves = dfs(stacks, 0, [])
print(min_moves)
