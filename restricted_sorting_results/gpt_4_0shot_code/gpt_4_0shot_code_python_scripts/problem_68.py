
from collections import deque
from copy import deepcopy

# Define the initial state of the stacks
stacks = [['Black', 'Black', 'White', 'Blue', 'Yellow', 'White'], ['Black', 'Blue', 'Red', 'Blue', 'Red', 'Green'], [], ['Black', 'White', 'Red', 'Green', 'White', 'Blue'], ['Yellow', 'Blue', 'Red', 'Green', 'Green', 'Yellow'], [], ['Green', 'Black', 'Red', 'White', 'Yellow', 'Yellow'], [], [], []]

# Define the cost of moving one block to the top of each stack
costs = {0: 9, 1: 11, 2: 2, 3: 10, 4: 8, 5: 6, 6: 4, 7: 4, 8: 7, 9: 3}

# Define a queue for the BFS algorithm
queue = deque([(stacks, [], 0)])

# Define a set to store visited states
visited = set()

while queue:
    # Pop the current state, the moves to reach it, and its cost from the queue
    current_stacks, current_moves, current_cost = queue.popleft()

    # If this state has been visited before, skip it
    if str(current_stacks) in visited:
        continue

    # Mark this state as visited
    visited.add(str(current_stacks))

    # Check if the current state is a goal state
    if all(len(set(stack)) <= 1 for stack in current_stacks if stack):
        # If it is, print the moves to reach it and its cost, and stop the algorithm
        print(current_moves, current_cost)
        break

    # For each pair of stacks
    for i in range(10):
        for j in range(10):
            # If the first stack is not empty and the second stack is either empty or its top block is the same color as the top block of the first stack
            if current_stacks[i] and (not current_stacks[j] or current_stacks[i][-1] == current_stacks[j][-1]):
                # Copy the current state and the moves to reach it
                new_stacks = deepcopy(current_stacks)
                new_moves = deepcopy(current_moves)

                # Move the top block from the first stack to the second stack
                new_stacks[j].append(new_stacks[i].pop())

                # Add the move to the list of moves
                new_moves.append((i, j))

                # Add the new state, the moves to reach it, and its cost to the queue
                queue.append((new_stacks, new_moves, current_cost + costs[j]))
