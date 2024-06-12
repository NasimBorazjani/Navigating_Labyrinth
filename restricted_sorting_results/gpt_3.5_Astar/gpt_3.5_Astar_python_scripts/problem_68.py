
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Black', 'Black', 'White', 'Blue', 'Yellow', 'White'],
                     ['Black', 'Blue', 'Red', 'Blue', 'Red', 'Green'],
                     [],
                     ['Black', 'White', 'Red', 'Green', 'White', 'Blue'],
                     ['Yellow', 'Blue', 'Red', 'Green', 'Green', 'Yellow'],
                     [],
                     ['Green', 'Black', 'Red', 'White', 'Yellow', 'Yellow'],
                     [],
                     [],
                     []]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 9, 1: 11, 2: 2, 3: 10, 4: 8, 5: 6, 6: 4, 7: 4, 8: 7, 9: 3}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(all(stack[i] == stack[i+1] for i in range(len(stack)-1)) for stack in state if stack):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    new_state = [list(stack) for stack in state]
                    if new_state[from_stack] and (not new_state[to_stack] or new_state[from_stack][-1] == new_state[to_stack][-1]):
                        block = new_state[from_stack].pop()
                        new_state[to_stack].append(block)
                        new_state = tuple(tuple(stack) for stack in new_state)
                        new_cost = g + max(1, stack_costs[from_stack])

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            h = heuristic(new_state)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state):
    # The heuristic is the sum of the costs of moving each block to the correct stack
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that each block can be moved to the correct stack in one step
    # The heuristic is consistent because the cost of moving a block to the correct stack is always at least 1, which is the decrease in the heuristic value
    h = 0
    for stack in state:
        for i in range(len(stack)-1):
            if stack[i] != stack[i+1]:
                h += 1
    return h


print(a_star())
