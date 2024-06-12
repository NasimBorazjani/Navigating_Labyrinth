
from collections import deque

def restricted_sorting(stacks, costs):
    # Define the goal state
    goal = [['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], [], []]

    # Initialize the BFS queue and the visited set
    queue = deque([(stacks, [], 0)])
    visited = set()

    while queue:
        # Pop the current state, path and cost from the queue
        state, path, cost = queue.popleft()

        # If this state is the goal state, return the path
        if state == goal:
            return path

        # If this state has been visited before, skip it
        if str(state) in visited:
            continue

        # Mark this state as visited
        visited.add(str(state))

        # Explore all possible next states
        for i in range(6):
            for j in range(6):
                if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]):
                    # Create a new state by transferring a block
                    new_state = [list(s) for s in state]
                    new_state[j].append(new_state[i].pop())
                    new_cost = cost + costs[j]
                    new_path = path + [(i, j)]

                    # Add the new state, path and cost to the queue
                    queue.append((new_state, new_path, new_cost))

    # If there is no solution, return an empty list
    return []

# Test the function
stacks = [['Blue', 'Green', 'Green', 'Red'], ['Yellow', 'Yellow', 'Green', 'Yellow'], [], [], [], ['Red', 'Blue', 'Red', 'Blue']]
costs = {0: 3, 1: 6, 2: 1, 3: 7, 4: 2, 5: 3}
print(restricted_sorting(stacks, costs))
