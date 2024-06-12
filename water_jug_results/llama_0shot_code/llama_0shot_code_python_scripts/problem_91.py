
from collections import deque

# capacities of the water jugs
jug_capacities = [51, 75, 112, 122, 54, 129, 31, 127, 113]

# target volumes for the buckets
bucket_volumes = [338, 431, 493, 550]

# initialize the queue with the initial state
queue = deque([([0]*len(bucket_volumes), [], 0)])

# keep track of the visited states
visited = set()

# perform the breadth-first search
while queue:
    state, actions, steps = queue.popleft()
    if state not in visited:
        visited.add(state)
        if state == bucket_volumes:
            # if we reached the target state, return the sequence of actions
            return actions
        for i, (jug, bucket) in enumerate(zip(jug_capacities, state)):
            # try adding water from the jug to the bucket
            if bucket < bucket_volumes[i]:
                new_state = list(state)
                new_state[i] += min(jug, bucket_volumes[i]-bucket)
                queue.append((tuple(new_state), actions + [('+', jug, i+1)], steps+1))
            # try removing water from the bucket
            if state[i] > 0:
                new_state = list(state)
                new_state[i] -= min(state[i], state[i+1] if i+1 < len(state) else float('inf'))
                queue.append((tuple(new_state), actions + [('-', jug, i+1)], steps+1))
