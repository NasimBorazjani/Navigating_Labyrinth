
from collections import deque

def bfs(initial_state, goal_state, costs):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        for i in range(len(state)):
            for j in range(len(state)):
                if i != j and state[i] and (not state[j] or state[i][-1] == state[j][-1]) and len(state[j]) < 6:
                    new_state = state[:]
                    new_state[j] = new_state[j] + [new_state[i].pop()]
                    new_state[i] = new_state[i][:]
                    if tuple(new_state) not in visited:
                        visited.add(tuple(new_state))
                        new_path = path + [(i, j, costs[j])]
                        queue.append((new_state, new_path))
    return []

initial_state = [[], [], ['Blue', 'Blue', 'Blue', 'Green', 'Black', 'Red'], [], ['Red', 'Black', 'Blue', 'White', 'Blue', 'Yellow'], ['Yellow', 'White', 'Green', 'Black', 'Yellow', 'Red'], [], [], ['White', 'Black', 'White', 'White', 'Black', 'Red'], ['Red', 'Green', 'Green', 'Yellow', 'Yellow', 'Green']]
goal_state = [['Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green', 'Green'], ['Black', 'Black', 'Black', 'Black', 'Black'], ['Red', 'Red', 'Red', 'Red', 'Red'], ['White', 'White', 'White', 'White', 'White'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], [], []]
costs = {0: 3, 1: 10, 2: 9, 3: 8, 4: 8, 5: 7, 6: 6, 7: 9, 8: 2, 9: 8}

print(bfs(initial_state, goal_state, costs))
