
from collections import deque
from copy import deepcopy

def solve(stacks):
    costs = {0: 7, 1: 6, 2: 2, 3: 7, 4: 7, 5: 4}
    start_state = tuple(map(tuple, stacks))
    visited = {start_state: (0, [])}
    queue = deque([start_state])

    while queue:
        state = queue.popleft()
        cost, moves = visited[state]
        stacks = list(map(list, state))

        for from_stack in range(6):
            if not stacks[from_stack]:
                continue
            block = stacks[from_stack][-1]

            for to_stack in range(6):
                if len(stacks[to_stack]) < 4 and (not stacks[to_stack] or stacks[to_stack][-1] == block):
                    new_stacks = deepcopy(stacks)
                    new_stacks[to_stack].append(new_stacks[from_stack].pop())
                    new_state = tuple(map(tuple, new_stacks))
                    new_cost = cost + costs[to_stack]
                    new_moves = moves + [(from_stack, to_stack)]

                    if new_state not in visited or new_cost < visited[new_state][0]:
                        visited[new_state] = (new_cost, new_moves)
                        queue.append(new_state)

    end_state = tuple(sorted([tuple(stack) for stack in stacks if stack]))
    return visited[end_state][1]

stacks = [[], [], ['Blue', 'Green', 'Yellow', 'Green'], ['Red', 'Yellow', 'Yellow', 'Green'], [], ['Red', 'Blue', 'Red', 'Blue']]
print(solve(stacks))
