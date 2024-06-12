
from collections import deque

# capacities of the jugs
jugs = [88, 125, 100, 62, 134, 89, 33, 133]

# capacities of the buckets
buckets = [306, 407, 457, 518]

# initialize the queue for BFS and the dictionary for parents
queue = deque([[0]*len(buckets)])
parents = {tuple([0]*len(buckets)): None}

# while there are still states to explore
while queue:
    # remove a state from the queue
    state = queue.popleft()

    # if this state is the goal state
    if state == buckets:
        # retrieve the shortest sequence of actions
        actions = []
        while state is not None:
            parent = parents[tuple(state)]
            if parent is not None:
                action = ('+', parent[1], parent[2]) if state[parent[2]] > parent[0] else ('-', parent[1], parent[2])
                actions.append(action)
                state = parent
        # reverse the list of actions to get the correct order
        actions.reverse()
        print(actions)
        break

    # generate all possible next states
    for i in range(len(jugs)):
        for j in range(len(buckets)):
            # try adding water from jug i to bucket j
            next_state = list(state)
            next_state[j] += jugs[i]
            if min(next_state) >= 0 and tuple(next_state) not in parents:
                parents[tuple(next_state)] = (jugs[i], i, j)
                queue.append(next_state)
            # try removing water from bucket j
            next_state = list(state)
            next_state[j] -= jugs[i]
            if min(next_state) >= 0 and tuple(next_state) not in parents:
                parents[tuple(next_state)] = (-jugs[i], i, j)
                queue.append(next_state)
