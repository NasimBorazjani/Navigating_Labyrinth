
from collections import deque

def bfs(jugs, buckets):
    # Initialize the queue with the initial state and the list of parents
    queue = deque([([0]*len(buckets), None)])
    parents = [{}]
    
    while queue:
        state, action = queue.popleft()
        
        # If this state is the final configuration, we have found a solution
        if state == buckets:
            return reconstruct_path(parents, action)
        
        # Generate all possible next states
        for i, (capacity, bucket) in enumerate(jugs):
            for j, target in enumerate(buckets):
                if state[j] + capacity <= target:
                    next_state = list(state)
                    next_state[j] += capacity
                    if tuple(next_state) not in parents:
                        queue.append((next_state, ('+', capacity, j)))
                        parents[tuple(next_state)] = (action, ('+', capacity, j))
                        
                if state[j] >= capacity and state[j] - capacity >= 0:
                    next_state = list(state)
                    next_state[j] -= capacity
                    if tuple(next_state) not in parents:
                        queue.append((next_state, ('-', capacity, j)))
                        parents[tuple(next_state)] = (action, ('-', capacity, j))
    
def reconstruct_path(parents, action):
    path = []
    while action is not None:
        path.append(action[1])
        action = parents[action[0]]
    return path[::-1]

jugs = [(67, 0), (55, 1), (84, 2), (148, 3), (107, 4), (114, 5), (17, 6), (143, 7), (40, 8), (39, 9)]
buckets = [192, 247, 479]

print(bfs(jugs, buckets))
