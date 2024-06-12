
import heapq

def initialize():
    initial_state = [['Pink', 'Black', 'Red', 'White', 'White', 'Black', 'Pink'], [], [], ['Green', 'Green', 'Blue', 'White', 'Pink', 'Pink', 'White'], [], ['Blue', 'Yellow', 'Yellow', 'Black', 'White', 'Green', 'Red'], ['Blue', 'Yellow', 'Blue', 'White', 'Green', 'Red', 'Pink'], ['Pink', 'Yellow', 'Yellow', 'Green', 'Green', 'Black', 'Blue'], [], ['Blue', 'Red', 'Red', 'Black', 'Black', 'Red', 'Yellow'], [], []]
    num_stacks = 12
    stack_capacity = 7
    move_costs = {0: 2, 1: 7, 2: 2, 3: 2, 4: 4, 5: 13, 6: 4, 7: 6, 8: 8, 9: 6, 10: 10, 11: 10}
    visited_costs = {}
    visited_costs[tuple((tuple(stack) for stack in initial_state))] = 0
    queue = [(0, 0, [], initial_state)]
    return (initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue)

def a_star():
    (initial_state, num_stacks, stack_capacity, move_costs, visited_costs, queue) = initialize()
    while queue:
        (_, g, actions, state) = heapq.heappop(queue)
        sorted_state = all((all(((stack[i] == stack[0]) for i in range(len(stack)))) for stack in state if stack))
        if sorted_state:
            return actions
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if (state[from_stack] and ((not state[to_stack]) or (state[to_stack][(- 1)] == state[from_stack][(- 1)])) and (len(state[to_stack]) < stack_capacity)):
                    new_state = [list(stack[:]) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(state[from_stack][(- 1)])
                    new_state = tuple((tuple(stack) for stack in new_state))
                    new_cost = (g + move_costs[from_stack])
                    if ((new_state not in visited_costs) or (new_cost < visited_costs[new_state])):
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost, new_cost, (actions + [(from_stack, to_stack)]), new_state))
    return None
print(a_star())
