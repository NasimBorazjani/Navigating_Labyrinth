
import heapq

def initialize():
    initial_state = (('Green', 'Black', 'White', 'Red', 'White', 'Yellow', 'Blue'), (), ('White', 'Pink', 'White', 'White', 'Green', 'Red', 'Blue'), (), ('Pink', 'Black', 'Black', 'White', 'Black', 'Green', 'Blue'), ('Pink', 'Green', 'Pink', 'Yellow', 'Yellow', 'Blue', 'Red'), (), ('Red', 'Yellow', 'Yellow', 'Yellow', 'Blue', 'Red', 'Black'), (), (), (), ('Red', 'Green', 'Black', 'Blue', 'Pink', 'Pink', 'Green'))
    num_stacks = 12
    stack_capacity = 7
    stack_costs = {0: 13, 1: 5, 2: 8, 3: 11, 4: 6, 5: 9, 6: 5, 7: 11, 8: 2, 9: 11, 10: 11, 11: 7}
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
