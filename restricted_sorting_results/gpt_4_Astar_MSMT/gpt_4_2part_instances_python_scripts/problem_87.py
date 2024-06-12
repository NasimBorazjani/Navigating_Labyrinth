
import heapq

def initialize():
    initial_state = (('Black', 'Blue', 'Pink', 'Green', 'Blue', 'Red', 'Red'), ('Yellow', 'White', 'White', 'Black', 'Yellow', 'Green', 'Green'), ('Yellow', 'Pink', 'White', 'Pink', 'Black', 'Red', 'Black'), (), ('Pink', 'Red', 'Blue', 'White', 'Blue', 'Blue', 'Red'), ('Blue', 'Yellow', 'White', 'Pink', 'Pink', 'Green', 'Green'), (), (), ('Yellow', 'Black', 'Yellow', 'White', 'Red', 'Black', 'Green'), (), (), ())
    num_stacks = 12
    stack_capacity = 7
    stack_costs = {0: 11, 1: 13, 2: 4, 3: 4, 4: 13, 5: 7, 6: 12, 7: 6, 8: 4, 9: 6, 10: 11, 11: 4}
    visited_costs = {}
    visited_costs[initial_state] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_stacks, stack_capacity, stack_costs, visited_costs, queue)

def a_star():
    (initial_state, num_stacks, stack_capacity, stack_costs, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        if all((((len(stack) == 0) or (len(set(stack)) == 1)) for stack in state)):
            return actions
        for from_stack_ind in range(num_stacks):
            if state[from_stack_ind]:
                for to_stack_ind in range(num_stacks):
                    if ((len(state[to_stack_ind]) < stack_capacity) and ((not state[to_stack_ind]) or (state[to_stack_ind][(- 1)] == state[from_stack_ind][(- 1)]))):
                        new_state = list((list(stack) for stack in state))
                        block = new_state[from_stack_ind].pop()
                        new_state[to_stack_ind].append(block)
                        new_state = tuple((tuple(stack) for stack in new_state))
                        new_cost = (g + stack_costs[to_stack_ind])
                        if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                            visited_costs[new_state] = new_cost
                            h = heuristic(new_state)
                            heapq.heappush(queue, ((new_cost + h), new_cost, (actions + [(from_stack_ind, to_stack_ind)]), new_state))
    return None

def heuristic(state):
    h = 0
    for stack in state:
        if stack:
            h += len([block for block in stack if (block != stack[(- 1)])])
    return h
print(a_star())
