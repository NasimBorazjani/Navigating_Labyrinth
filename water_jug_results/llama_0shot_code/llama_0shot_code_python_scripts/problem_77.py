
from collections import deque

def bfs(capacities):
    initial_state = [0, 0, 0, 0]
    goal_state = [166, 239, 286, 421]
    queue = deque([(initial_state, '')])
    shortest_path = {str(initial_state): ''}

    while queue:
        state, action = queue.popleft()
        if state == goal_state:
            return action
        for i, (capacity, _) in enumerate(capacities):
            for j, (_, amount) in enumerate(state):
                if amount + capacity <= goal_state[i]:
                    new_state = list(state)
                    new_state[j] += capacity
                    if str(new_state) not in shortest_path:
                        queue.append((new_state, action + f" ('+', {capacity}, {j+1}), "))
                        shortest_path[str(new_state)] = action + f" ('+', {capacity}, {j+1}), "
                if amount >= capacity:
                    new_state = list(state)
                    new_state[j] -= capacity
                    if str(new_state) not in shortest_path:
                        queue.append((new_state, action + f" ('-', {capacity}, {j+1}), "))
                        shortest_path[str(new_state)] = action + f" ('-', {capacity}, {j+1}), "

capacities = [(60, 'A'), (59, 'B'), (72, 'C'), (93, 'D'), (39, 'E'), (74, 'F'), (71, 'G'), (84, 'H')]
print(bfs(capacities))
