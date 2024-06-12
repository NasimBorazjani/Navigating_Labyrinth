
from collections import deque

def bfs():
    # Initialize the unlabeled buckets and the jugs.
    buckets = [0, 0, 0]
    jugs = [33, 56, 108, 53, 65, 54, 52, 59]

    # The final state.
    final_buckets = [168, 239, 307]

    # Create a queue for BFS and add the initial state to the queue.
    queue = deque([(buckets, [])])

    # Create a set to store the visited states.
    visited = set()

    while queue:
        # Remove a state from the queue.
        buckets, actions = queue.popleft()

        # If this state is the final state, we have found the shortest sequence of actions.
        if buckets == final_buckets:
            return actions

        # Generate all possible next states by performing all possible actions.
        for i in range(len(jugs)):
            for j in range(len(buckets)):
                for action in [('+', i), ('-', i)]:
                    new_buckets, new_actions = fill_or_empty(buckets, jugs[i], j, action, actions)
                    if new_buckets is not None:
                        # Add the new state to the queue and the set if it has not been visited.
                        if tuple(new_buckets) not in visited:
                            queue.append((new_buckets, new_actions))
                            visited.add(tuple(new_buckets))

    # If we have visited all possible states and have not found the final state, there is no solution.
    return None

def fill_or_empty(buckets, jug_capacity, bucket_index, action, actions):
    new_buckets = buckets[:]
    new_actions = actions[:]
    if action[0] == '+':
        # Try to fill the bucket.
        if bucket_index < len(buckets) - 1 and buckets[bucket_index + 1] >= jug_capacity:
            return None, None
        if new_buckets[bucket_index] + jug_capacity <= jug_capacity:
            new_buckets[bucket_index] += jug_capacity
            new_actions.append((action[0], jug_capacity, bucket_index + 1))
        else:
            return None, None
    else:
        # Try to empty the bucket.
        if new_buckets[bucket_index] - jug_capacity < 0:
            return None, None
        new_buckets[bucket_index] -= jug_capacity
        new_actions.append((action[0], jug_capacity, bucket_index + 1))
    return new_buckets, new_actions

print(bfs())
