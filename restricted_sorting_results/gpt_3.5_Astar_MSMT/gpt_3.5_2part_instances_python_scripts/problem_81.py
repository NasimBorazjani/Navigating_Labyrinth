
import heapq

def initialize():
    initial_state = [[], ['White', 'Black', 'Yellow', 'Black', 'Green', 'Blue', 'Pink'], ['Black', 'Red', 'Yellow', 'White', 'Yellow', 'Black', 'Green'], ['Yellow', 'White', 'Green', 'White', 'White', 'Black', 'Blue'], ['Blue', 'Pink', 'Red', 'Pink', 'Green', 'Yellow', 'Black'], ['White', 'Red', 'Pink', 'Blue', 'Blue', 'Pink', 'Green'], [], [], [], ['Red', 'Pink', 'Red', 'Blue', 'Red', 'Green', 'Yellow'], [], []]
    num_stacks = 12
    stack_capacity = 7
    move_costs = {0: 5, 1: 3, 2: 3, 3: 4, 4: 2, 5: 2, 6: 12, 7: 9, 8: 5, 9: 11, 10: 11, 11: 10}
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
