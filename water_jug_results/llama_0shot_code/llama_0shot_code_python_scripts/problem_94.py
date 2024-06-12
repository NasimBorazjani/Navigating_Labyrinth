
from collections import deque

def shortest_sequence(capacities, targets):
    # Initialize the queue with the initial state and the list of visited states
    queue = deque([([0]*len(targets), 0, [])])
    visited = set()

    while queue:
        # Dequeue a state
        (buckets, steps, actions) = queue.popleft()

        # If this state has not been visited before
        if tuple(buckets) not in visited:
            # Mark it as visited
            visited.add(tuple(buckets))

            # If all buckets are filled with the correct amounts of water
            if buckets == targets:
                # Return the shortest sequence of actions
                return actions

            # Enqueue all possible next states
            for i, (capacity, target) in enumerate(zip(capacities, targets)):
                for j in range(len(buckets)):
                    if buckets[j] + capacity <= target:
                        new_buckets = list(buckets)
                        new_buckets[j] += capacity
                        queue.append((new_buckets, steps + 1, actions + [('+', capacity, j+1)]))
                    if buckets[j] >= capacity:
                        new_buckets = list(buckets)
                        new_buckets[j] -= capacity
                        queue.append((new_buckets, steps + 1, actions + [('-', capacity, j+1)]))

    # If there is no solution
    return None

capacities = [81, 56, 41, 88, 137, 14, 149, 120, 87, 104]
targets = [377, 456, 512, 541]

actions = shortest_sequence(capacities, targets)
print(actions)
