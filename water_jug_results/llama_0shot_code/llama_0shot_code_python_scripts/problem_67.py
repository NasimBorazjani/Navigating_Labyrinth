
from collections import deque

def bfs():
    # Define the capacities of the jugs and the amounts of water in the buckets
    capacities = [116, 115, 29, 129, 39, 114]
    amounts = [353, 368, 396, 403]

    # Define the initial state and the goal state
    initial_state = ([0]*len(amounts), capacities)
    goal_state = (amounts, capacities)

    # Create a queue for BFS and add the initial state to the queue
    queue = deque([(initial_state, [])])

    # Create a set to store visited states
    visited = set()

    # Perform BFS
    while queue:
        (state, actions) = queue.popleft()
        if state not in visited:
            visited.add(state)
            if state == goal_state:
                return actions
            for action in generate_next_states(state):
                queue.append((action, actions + [action]))

    # If there is no solution, return None
    return None

def generate_next_states(state):
    (amounts, capacities) = state
    next_states = []
    for i in range(len(amounts)):
        for j in range(len(capacities)):
            for action in ['+', '-']:
                if action == '+':
                    new_amounts = list(amounts)
                    new_amounts[i] += min(capacities[j], amounts[i])
                    next_states.append((new_amounts, capacities))
                else:
                    if amounts[i] >= capacities[j]:
                        new_amounts = list(amounts)
                        new_amounts[i] -= capacities[j]
                        next_states.append((new_amounts, capacities))
    return next_states

# Test the function
actions = bfs()
if actions is not None:
    print(actions)
else:
    print("No solution found")
