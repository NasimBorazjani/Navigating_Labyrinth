
from collections import deque

def bfs(jugs, buckets):
    # Initialize queue and parent dictionary
    queue = deque([([0]*len(buckets))])
    parent = {tuple([0]*len(buckets)): None}
    
    while queue:
        state = queue.popleft()
        if state == buckets:
            # We have found a solution
            break
        for i, (jug, bucket) in enumerate(zip(jugs, state)):
            for action in [('+', jug), ('-', jug)]:
                if action[0] == '+' and state[i] + jug < bucket:
                    # We can fill the jug
                    new_state = list(state)
                    new_state[i] += jug
                    if tuple(new_state) not in parent:
                        queue.append(new_state)
                        parent[tuple(new_state)] = (action[0], action[1], i)
                elif action[0] == '-' and state[i] - jug >= 0:
                    # We can empty the jug
                    new_state = list(state)
                    new_state[i] -= jug
                    if tuple(new_state) not in parent:
                        queue.append(new_state)
                        parent[tuple(new_state)] = (action[0], action[1], i)
    
    # Backtrack to find the sequence of actions
    actions = []
    while parent[tuple(buckets)] is not None:
        actions.append(parent[tuple(buckets)])
        buckets[actions[-1][2]] -= actions[-1][1] if actions[-1][0] == '+' else -actions[-1][1]
    return actions[::-1]

jugs = [51, 129, 150, 138, 128, 72, 69, 111, 75]
buckets = [454, 547, 601]
print(bfs(jugs, buckets))
