
import heapq
from collections import defaultdict

def restricted_sorting(stacks):
    costs = {0: 4, 1: 5, 2: 2, 3: 10, 4: 6, 5: 8, 6: 2, 7: 11, 8: 2, 9: 8}
    moves = defaultdict(list)
    prev = {}
    queue = [(0, tuple(tuple(stack) for stack in stacks))]
    visited = set(queue)

    while queue:
        cost, state = heapq.heappop(queue)
        if all(len(stack) <= 1 or all(block == stack[1] for block in stack) for stack in state):
            path = []
            while state in prev:
                path.append(moves[state])
                state = prev[state]
            return path[::-1]
        for i, stack in enumerate(state):
            if stack:
                for j, dest in enumerate(state):
                    if i != j and (not dest or dest[0] == stack[0]) and len(dest) < 6:
                        new_state = list(list(s) for s in state)
                        new_state[i] = new_state[i][1:]
                        new_state[j] = [stack[0]] + new_state[j]
                        new_state = tuple(tuple(s) for s in new_state)
                        if new_state not in visited:
                            heapq.heappush(queue, (cost - costs[j], new_state))
                            visited.add(new_state)
                            prev[new_state] = state
                            moves[new_state] = (i, j)
    return []

stacks = [[], [], ['White', 'Black', 'Green', 'White', 'Green', 'Blue'], ['Red', 'Green', 'Black', 'Red', 'White', 'Yellow'], [], ['Yellow', 'Black', 'Yellow', 'Red', 'Green', 'White'], [], ['White', 'Blue', 'Red', 'Red', 'Blue', 'Black'], [], ['Yellow', 'Blue', 'Yellow', 'Blue', 'Green', 'Black']]
print(restricted_sorting(stacks))
