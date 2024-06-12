
from collections import deque
from copy import deepcopy

def is_goal_state(state):
    for stack in state:
        if len(set(stack)) > 1:
            return False
    return True

def get_moves(state, costs):
    moves = []
    for i, stack in enumerate(state):
        if stack:
            for j, cost in enumerate(costs):
                if i != j and (not state[j] or state[j][-1] == stack[-1]):
                    new_state = deepcopy(state)
                    new_state[j].append(new_state[i].pop())
                    moves.append((new_state, cost, (i, j)))
    return moves

def restricted_sorting(stacks, costs):
    initial_state = [deque(stack) for stack in stacks]
    queue = deque([(initial_state, 0, [])])
    visited = set()

    while queue:
        state, cost, path = queue.popleft()
        state_tuple = tuple(tuple(stack) for stack in state)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if is_goal_state(state):
            return path

        for new_state, new_cost, move in get_moves(state, costs):
            queue.append((new_state, cost + new_cost, path + [move]))

    return None

stacks = [[], ['Blue', 'Black', 'Black', 'Yellow', 'White', 'Green'], ['Green', 'Black', 'Red', 'Green', 'Yellow', 'Blue'], [], ['Green', 'Red', 'Blue', 'Yellow', 'Green', 'Blue'], ['Black', 'White', 'White', 'Red', 'White', 'Black'], [], ['White', 'Red', 'Blue', 'Yellow', 'Yellow', 'Red'], [], []]
costs = [5, 4, 7, 7, 11, 11, 8, 3, 7, 9]
print(restricted_sorting(stacks, costs))
