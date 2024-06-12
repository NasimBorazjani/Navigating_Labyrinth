
from collections import deque

def bfs():
    # Define the capacities of the jugs and the amounts of water in the unlabeled buckets
    capacities = [43, 149, 131, 132, 70, 104]
    goals = [284, 297, 436]

    # Define the initial state and the goal state
    initial_state = ([0]*3, [0]*6)
    goal_state = ([284, 297, 436], [0]*6)

    # Create a queue for BFS and add the initial state to it
    queue = deque([(initial_state, [])])

    # While the queue is not empty
    while queue:
        # Remove a state from the queue
        (unlabeled, jugs), actions = queue.popleft()

        # If this state is the goal state
        if unlabeled == goal_state[0]:
            # Return the sequence of actions that led to it
            return actions

        # Generate all possible next states
        for i in range(len(capacities)):
            for j in range(3):
                # Try adding water from the jug with capacity capacities[i] to the unlabeled bucket numbered j+1
                new_unlabeled = unlabeled[:]
                new_unlabeled[j] += capacities[i]
                new_jugs = jugs[:]
                new_jugs[i] -= capacities[i]
                if new_unlabeled[j] <= goals[j] and new_jugs[i] >= 0:
                    queue.append(((new_unlabeled, new_jugs), actions + [('+', capacities[i], j+1)]))

                # If the unlabeled bucket numbered j+1 is not empty
                if unlabeled[j] > 0:
                    # Try removing water from the unlabeled bucket numbered j+1
                    new_unlabeled = unlabeled[:]
                    new_unlabeled[j] -= min(unlabeled[j], capacities[i])
                    queue.append(((new_unlabeled, jugs), actions + [('-', capacities[i], j+1)]))

    # If there is no solution, return an empty list
    return []

print(bfs())
