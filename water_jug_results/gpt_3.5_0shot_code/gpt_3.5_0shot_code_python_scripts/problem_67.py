
from collections import deque

# Define the capacities of the jugs and unlabeled buckets
jugs = [116, 115, 29, 129, 39, 114]
buckets = [353, 368, 396, 403]

# Initialize a queue to store the states of the buckets and actions taken
queue = deque([(0, 0, 0, 0, [])])

# Initialize a set to store visited states
visited = set()

# Perform BFS to find the shortest sequence of actions
while queue:
    state = queue.popleft()
    
    if state[:4] == tuple(buckets):
        print(state[4])
        break
    
    if state[:4] in visited:
        continue
    
    visited.add(state[:4])
    
    for i in range(5):
        for j in range(5):
            if i != j:
                new_state = list(state)
                
                if state[i] > 0 and state[j] < jugs[j]:
                    amount = min(state[i], jugs[j] - state[j])
                    new_state[i] -= amount
                    new_state[j] += amount
                    new_state[4].append(('+', jugs[i], jugs[j]))
                    queue.append(tuple(new_state))

                if state[j] > 0 and state[i] < jugs[i]:
                    amount = min(state[j], jugs[i] - state[i])
                    new_state[j] -= amount
                    new_state[i] += amount
                    new_state[4].append(('-', jugs[j], jugs[i]))
                    queue.append(tuple(new_state))
