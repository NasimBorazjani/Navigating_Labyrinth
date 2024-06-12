
from collections import deque

# capacities of the water jugs
jug_capacities = [39, 110, 41, 54, 47, 33, 136, 40, 100]

# target amounts for the buckets
bucket_targets = [192, 459, 473, 493]

# initialize the queue with the initial state
queue = deque([([0]*len(bucket_targets), [])])

# while there are still states to process
while queue:
    # dequeue the first state
    (buckets, actions) = queue.popleft()

    # if this state is the final state
    if buckets == bucket_targets:
        # we have found a solution
        # print the sequence of actions that led to this state
        print(actions)
        break

    # try to fill each bucket from each jug
    for i in range(len(buckets)):
        for j in range(len(jug_capacities)):
            # calculate the amount of water to add or remove
            delta = min(jug_capacities[j], bucket_targets[i] - buckets[i])
            # if this change is possible
            if delta > 0:
                # transition to a new state
                new_buckets = list(buckets)
                new_buckets[i] += delta
                new_actions = list(actions)
                new_actions.append(('+', jug_capacities[j], i+1))
                # enqueue the new state
                queue.append((new_buckets, new_actions))

            delta = min(buckets[i], bucket_targets[i] - buckets[i])
            if delta > 0:
                new_buckets = list(buckets)
                new_buckets[i] -= delta
                new_actions = list(actions)
                new_actions.append(('-', jug_capacities[j], i+1))
                queue.append((new_buckets, new_actions))
