
from collections import deque
from copy import deepcopy

# Define the initial state of the stacks
stacks = [['Yellow', 'Green', 'White', 'Pink', 'Black', 'Pink', 'Pink'], ['Pink', 'Red', 'White', 'Black', 'Green', 'White', 'Pink'], ['Red', 'Black', 'Green', 'Blue', 'Red', 'Black', 'Yellow'], ['Blue', 'White', 'Blue', 'Blue', 'Black', 'White', 'Blue'], ['Yellow', 'Blue', 'Green', 'Green', 'Red', 'Red', 'Yellow'], [], [], [], ['Black', 'Yellow', 'Red', 'Green', 'Yellow', 'Pink', 'White'], [], [], []]
# Define the cost of moving one block to the top of each stack
costs = {0: 11, 1: 11, 2: 12, 3: 4, 4: 12, 5: 2, 6: 10, 7: 8, 8: 6, 9: 10, 10: 8, 11: 3}

# Define the BFS queue and the visited set
queue = deque([(stacks, [], 0)])
visited = set()

while queue:
    # Pop the current state, path and cost from the queue
    stacks, path, cost = queue.popleft()
    # Convert the current state to a tuple and check if it has been visited
    state = tuple(tuple(stack) for stack in stacks)
    if state in visited:
        continue
    visited.add(state)
    # Check if the current state is a goal state
    if all(len(set(stack)) <= 1 for stack in stacks):
        print(path)
        break
    # Generate all possible moves from the current state
    for i in range(12):
        if stacks[i]:
            for j in range(12):
                if i != j and (not stacks[j] or stacks[j][-1] == stacks[i][-1]) and len(stacks[j]) < 7:
                    # Make a copy of the current state and path
                    new_stacks = deepcopy(stacks)
                    new_path = path[:]
                    # Move a block from stack i to stack j
                    new_stacks[j].append(new_stacks[i].pop())
                    new_path.append((i, j))
                    # Add the new state, path and cost to the queue
                    queue.append((new_stacks, new_path, cost + costs[j]))
