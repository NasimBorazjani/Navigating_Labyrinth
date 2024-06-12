
from collections import deque
from copy import deepcopy

# Define the cost of moving a block to each stack
costs = {0: 5, 1: 5, 2: 5, 3: 6, 4: 5, 5: 5, 6: 9, 7: 6}

# Define the initial state of the stacks
stacks = [[], ['Yellow', 'Red', 'Black', 'Yellow', 'Green'], [], [], ['Green', 'Red', 'Blue', 'Blue', 'Black'], ['Green', 'Blue', 'Yellow', 'Red', 'Yellow'], [], ['Blue', 'Green', 'Black', 'Red', 'Black']]

# Define the queue for the BFS algorithm
queue = deque([(stacks, [], 0)])

# Define the set of visited states
visited = set()

while queue:
    # Pop the next state from the queue
    stacks, moves, cost = queue.popleft()

    # Convert the state to a tuple for hashing
    state = tuple(tuple(stack) for stack in stacks)

    # If we have visited this state before, skip it
    if state in visited:
        continue

    # Add the state to the set of visited states
    visited.add(state)

    # If all stacks are sorted, return the moves
    if all(len(set(stack)) <= 1 for stack in stacks if stack):
        print(moves)
        break

    # Try moving a block from each stack to each other stack
    for i, stack in enumerate(stacks):
        if stack:
            for j, target in enumerate(stacks):
                if i != j and (not target or target[-1] == stack[-1]) and len(target) < 5:
                    # Create a copy of the stacks and moves
                    new_stacks = deepcopy(stacks)
                    new_moves = moves[:]

                    # Move the block
                    new_stacks[j].append(new_stacks[i].pop())

                    # Add the move to the list of moves
                    new_moves.append((i, j))

                    # Add the new state to the queue
                    queue.append((new_stacks, new_moves, cost + costs[j]))
