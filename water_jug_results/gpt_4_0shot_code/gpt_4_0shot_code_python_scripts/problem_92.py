
from collections import deque

jugs = [143, 34, 117, 130, 50, 142, 144, 150, 29, 78]
buckets = [0, 0, 0, 0]
goal = [307, 316, 325, 622]

def bfs():
    queue = deque([buckets])
    actions = {tuple(buckets): []}
    
    while queue:
        state = queue.popleft()
        
        if list(state) == goal:
            return actions[state]
        
        for i in range(len(jugs)):
            for j in range(len(buckets)):
                if state[j] + jugs[i] <= goal[j] and all(state[j] + jugs[i] >= state[k] for k in range(j+1, len(buckets))):
                    new_state = list(state)
                    new_state[j] += jugs[i]
                    new_state = tuple(new_state)
                    
                    if new_state not in actions:
                        queue.append(new_state)
                        actions[new_state] = actions[state] + [('+', jugs[i], j+1)]
                
                if state[j] > 0:
                    new_state = list(state)
                    new_state[j] = 0
                    new_state = tuple(new_state)
                    
                    if new_state not in actions:
                        queue.append(new_state)
                        actions[new_state] = actions[state] + [('-', jugs[i], j+1)]
    
    return None

print(bfs())
