
from collections import deque

def bfs():
    # Define the capacities of the jugs and the amounts of water in the buckets
    capacities = [59, 20, 21, 62, 61, 60]
    amounts = [149, 156, 173, 186]

    # Define the initial state and the goal state
    initial_state = ([0]*len(amounts), [0]*len(capacities))
    goal_state = (amounts, [0]*len(capacities))

    # Create a queue for BFS and put the initial state into the queue
    queue = deque([(initial_state, [])])

    # Create a set to store visited states
    visited = set()

    while queue:
        # Remove a state from the queue
        (buckets, jugs), actions = queue.popleft()

        # If this state is the goal state, we have found the shortest sequence of actions
        if buckets == goal_state[0]:
            return actions

        # Generate all possible next states
        for i in range(len(capacities)):
            for j in range(len(buckets)):
                if buckets[j] < amounts[j]:
                    # Try to fill the bucket from the jug
                    new_buckets = list(buckets)
                    new_buckets[j] += min(amounts[j] - buckets[j], capacities[i] - jugs[i])
                    new_jugs = list(jugs)
                    new_jugs[i] = capacities[i]
                    new_state = (tuple(new_buckets), tuple(new_jugs))
                    new_actions = actions + [('+', capacities[i], j+1)]
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, new_actions))
                elif buckets[j] > amounts[j]:
                    # Try to empty the bucket into the jug
                    new_buckets = list(buckets)
                    new_buckets[j] -= min(buckets[j] - amounts[j], jugs[i])
                    new_jugs = list(jugs)
                    new_jugs[i] += min(buckets[j] - amounts[j], jugs[i])
                    new_state = (tuple(new_buckets), tuple(new_jugs))
                    new_actions = actions + [('-', capacities[i], j+1)]
                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, new_actions))

    # If we have processed all states and have not found the goal state, it is impossible to reach it
    return None

# Call the function and print the result
actions = bfs()
if actions is None:
    print("It is impossible to reach the goal state.")
else:
    print("The shortest sequence of actions is:", actions)
