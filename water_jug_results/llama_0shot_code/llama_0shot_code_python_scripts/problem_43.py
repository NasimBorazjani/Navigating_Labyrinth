
from collections import deque

# capacities of the water jugs
jug_capacities = [104, 14, 83, 46, 128, 34, 137, 15, 19, 126]

# target amounts for the unlabeled buckets
target_amounts = [342, 373, 447]

# initialize the queue with the initial state
queue = deque([([0]*len(target_amounts), [])])

# while there are still states to process
while queue:
    # dequeue the first state
    (buckets, actions) = queue.popleft()

    # if this state is the desired final state
    if buckets == target_amounts:
        # we have found the shortest sequence of actions, so we can stop
        print(actions)
        break

    # try to fill each unlabeled bucket from each jug
    for i, (bucket, amount) in enumerate(zip(buckets, target_amounts)):
        for j, jug in enumerate(jug_capacities):
            # if the jug can fill the bucket without exceeding the capacity
            if bucket + jug <= amount and bucket + jug <= target_amounts[i+1]:
                # enqueue the new state
                queue.append((list(buckets), actions + [('+', jug, i+1)]))

    # try to empty each unlabeled bucket
    for i, (bucket, amount) in enumerate(zip(buckets, target_amounts)):
        for j in range(1, min(bucket, target_amounts[i+1])+1):
            # enqueue the new state
            queue.append(([bucket-j if k==i else bucket for k, bucket in enumerate(buckets)], actions + [('-', j, i+1)]))
