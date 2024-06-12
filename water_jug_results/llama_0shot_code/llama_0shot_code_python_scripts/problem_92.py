
from collections import deque

# capacities of the water jugs
jug_capacities = [143, 34, 117, 130, 50, 142, 144, 150, 29, 78]

# target amounts for the unlabeled buckets
target_amounts = [307, 316, 325, 622]

# initialize the queue with the initial state
queue = deque([([0]*len(target_amounts), [])])

# while there are still states to process
while queue:
    # dequeue the first state
    amounts, actions = queue.popleft()

    # if this state is the final state
    if amounts == target_amounts:
        # we have found a solution, so we return the sequence of actions
        return actions

    # otherwise, we apply all possible actions to transition to new states
    for i, (capacity, target) in enumerate(zip(jug_capacities, target_amounts)):
        # if the current amount is less than the target amount
        if amounts[i] < target:
            # we try to fill the bucket with the current jug
            new_amounts = list(amounts)
            new_amounts[i] += min(capacity, target - amounts[i])
            queue.append((new_amounts, actions + [('+', capacity, i+1)]))

        # if the current amount is more than the target amount
        elif amounts[i] > target:
            # we try to empty the bucket into the current jug
            new_amounts = list(amounts)
            new_amounts[i] -= min(amounts[i] - target, capacity)
            queue.append((new_amounts, actions + [('-', capacity, i+1)]))
