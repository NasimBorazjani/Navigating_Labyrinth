
from collections import deque

def restricted_sorting(stacks):
    costs = {0: 3, 1: 5, 2: 1, 3: 6, 4: 7, 5: 4}
    initial_state = tuple(map(tuple, stacks))
    goal_state = ((), ('Blue', 'Blue', 'Blue'), (), ('Green', 'Green', 'Green'), (), ('Red', 'Red', 'Red', 'Yellow', 'Yellow', 'Yellow'))
    queue = deque([(initial_state, 0, [])])
    predecessors = {initial_state: (None, None)}
    while queue:
        state, cost, path = queue.popleft()
        if state == goal_state:
            return path
        for i in range(6):
            if not state[i]:
                continue
            for j in range(6):
                if i != j and (not state[j] or state[j][-1] == state[i][-1]) and len(state[j]) < 4:
                    new_state = list(map(list, state))
                    block = new_state[i].pop()
                    new_state[j].append(block)
                    new_state = tuple(map(tuple, new_state))
                    new_cost = cost + costs[j]
                    if new_state not in predecessors or new_cost < predecessors[new_state][1]:
                        predecessors[new_state] = (state, (i, j))
                        queue.append((new_state, new_cost, path + [(i, j)]))
    return None

stacks = [[], ['Blue', 'Blue', 'Green', 'Red'], [], ['Green', 'Red', 'Yellow', 'Yellow'], [], ['Green', 'Red', 'Blue', 'Yellow']]
print(restricted_sorting(stacks))
