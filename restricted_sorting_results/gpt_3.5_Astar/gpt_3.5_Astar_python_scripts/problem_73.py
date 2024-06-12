
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Black', 'Red', 'Black', 'Green', 'Blue', 'Yellow'],
                     ['Yellow', 'Yellow', 'Black', 'Blue', 'Red', 'Green'],
                     [],
                     [],
                     [],
                     [],
                     ['Yellow', 'Black', 'White', 'Yellow', 'Red', 'Black'],
                     ['Green', 'Blue', 'Green', 'White', 'Blue', 'Green'],
                     ['Red', 'White', 'Blue', 'White', 'White', 'Red'],
                     []]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 11, 1: 8, 2: 4, 3: 6, 4: 4, 5: 3, 6: 6, 7: 9, 8: 5, 9: 10}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if all stacks are sorted
        if all(stack == sorted(stack, key=lambda x: (x != 'Black', x != 'Red', x != 'Green', x != 'Blue', x != 'Yellow', x != 'White')) for stack in state):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if transferring a block from the 'from_stack' to the 'to_stack' is valid
                    if state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                        new_state = [list(stack) for stack in state]
                        new_state[from_stack].pop()
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the new state
                        new_cost = g + stack_costs[to_stack]

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Calculate the heuristic cost
                            h = heuristic(new_state)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state):
    # The heuristic is the sum of the costs of moving the blocks to their correct positions
    # The heuristic is admissible because it never overestimates the cost to reach the goal state
    # The heuristic is consistent because the cost of moving a block to the correct position is always at least 1, which is the decrease in the heuristic estimate
    h = 0
    for stack in state:
        for i, block in enumerate(stack):
            if block != sorted(stack, key=lambda x: (x != 'Black', x != 'Red', x != 'Green', x != 'Blue', x != 'Yellow', x != 'White'))[i]:
                h += 1
    return h


print(a_star())
