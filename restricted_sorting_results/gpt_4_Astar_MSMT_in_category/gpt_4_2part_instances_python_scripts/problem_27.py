
import heapq
from collections import Counter

def initialize():
    initial_state = (('Red', 'Blue', 'Green', 'Yellow'), ('Blue', 'Blue', 'Green', 'Red'), (), (), (), ('Green', 'Red', 'Yellow', 'Yellow'))
    num_stacks = 6
    capacity = 4
    stack_costs = {0: 3, 1: 6, 2: 2, 3: 4, 4: 6, 5: 5}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_stacks, capacity, stack_costs, visited_costs, queue)

def a_star():
    (initial_state, num_stacks, capacity, stack_costs, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if all(((len(set(stack)) <= 1) for stack in state)):
            return actions
        for from_stack_ind in range(num_stacks):
            for to_stack_ind in range(num_stacks):
                if ((from_stack_ind != to_stack_ind) and state[from_stack_ind] and (len(state[to_stack_ind]) < capacity)):
                    new_state = [list(stack[:]) for stack in state]
                    block_to_move = new_state[from_stack_ind].pop(0)
                    new_state[to_stack_ind].insert(0, block_to_move)
                    new_state = tuple((tuple(stack) for stack in new_state))
                    new_cost = (g + stack_costs[to_stack_ind])
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, ((new_cost + heuristic(new_state)), (g + 1), (actions + [(from_stack_ind, to_stack_ind)]), new_state))
    return None

def heuristic(stacks):
    h = 0
    for stack in stacks:
        if stack:
            reversed_stack = stack[:]
            reversed_stack = reversed_stack[::(- 1)]
            most_common_color = Counter(reversed_stack).most_common(1)[0][0]
            for block in stack:
                if (block != most_common_color):
                    h += 1
    return h
print(a_star())
