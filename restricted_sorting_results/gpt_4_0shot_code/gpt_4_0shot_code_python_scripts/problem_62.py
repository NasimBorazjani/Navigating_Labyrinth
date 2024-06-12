
from queue import PriorityQueue

def restricted_sorting(stacks, costs):
    # Initialize the priority queue with the initial state
    queue = PriorityQueue()
    queue.put((0, stacks, []))

    # Keep track of visited states to avoid cycles
    visited = set()

    while not queue.empty():
        # Get the state with the least cost
        cost, stacks, moves = queue.get()

        # Convert the state to a tuple to be able to store it in a set
        state = tuple(tuple(stack) for stack in stacks)

        # If this state has been visited before, skip it
        if state in visited:
            continue

        # Mark this state as visited
        visited.add(state)

        # If this state is a goal state, return the moves that lead to it
        if all(len(set(stack)) <= 1 for stack in stacks if stack):
            return moves

        # Try all possible moves
        for i, stack in enumerate(stacks):
            if stack:
                for j, target in enumerate(stacks):
                    if i != j and (not target or target[-1] == stack[-1]) and len(target) < 6:
                        # Make a copy of the stacks and the moves
                        new_stacks = [list(s) for s in stacks]
                        new_moves = list(moves)

                        # Move a block from stack i to stack j
                        new_stacks[j].append(new_stacks[i].pop())

                        # Add the move to the list of moves
                        new_moves.append((i, j))

                        # Add the new state to the queue with its cost
                        new_cost = cost + costs[j]
                        queue.put((new_cost, new_stacks, new_moves))

    # If the queue is empty, there is no solution
    return None

# Test the function
stacks = [[], [], ['Blue', 'Yellow', 'Red', 'Black', 'White', 'Blue'], ['Blue', 'Green', 'Yellow', 'Red', 'Red', 'White'], [], ['Red', 'Black', 'White', 'Yellow', 'White', 'Green'], [], ['Black', 'Yellow', 'Green', 'Black', 'Black', 'Blue'], [], ['Red', 'Green', 'Green', 'Blue', 'Yellow', 'White']]
costs = {0: 6, 1: 10, 2: 8, 3: 3, 4: 5, 5: 7, 6: 10, 7: 6, 8: 3, 9: 8}
print(restricted_sorting(stacks, costs))
