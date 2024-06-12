
from heapq import heappop, heappush

def restricted_sorting(stacks):
    costs = {0: 6, 1: 3, 2: 5, 3: 2, 4: 8, 5: 3, 6: 8, 7: 5}
    goal = [['Yellow']*4, ['Blue']*4, ['Green']*4, ['Red']*4, ['Black']*4, [], [], []]
    queue = [(0, stacks, [])]
    visited = set()

    while queue:
        cost, state, path = heappop(queue)
        if state == goal:
            return path
        for i in range(8):
            if state[i]:
                block = state[i][-1]
                for j in range(8):
                    if i != j and (not state[j] or state[j][-1] == block) and len(state[j]) < 5:
                        new_state = [s[:] for s in state]
                        new_state[i].pop()
                        new_state[j].append(block)
                        new_cost = cost + costs[j]
                        new_path = path + [(i, j)]
                        if tuple(new_state) not in visited:
                            visited.add(tuple(new_state))
                            heappush(queue, (new_cost, new_state, new_path))

stacks = [[], ['Yellow', 'Blue', 'Blue', 'Yellow', 'Green'], ['Black', 'Red', 'Black', 'Green', 'Red'], ['Yellow', 'Yellow', 'Red', 'Black', 'Blue'], [], ['Blue', 'Red', 'Green', 'Green', 'Black'], [], []]
print(restricted_sorting(stacks))
