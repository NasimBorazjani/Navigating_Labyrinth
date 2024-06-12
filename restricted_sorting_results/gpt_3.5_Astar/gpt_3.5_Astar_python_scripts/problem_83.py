
import heapq
import math


def a_star():
    # Define the initial state of the stacks, with the shade of the topmost block in each stack
    initial_state = [[],
                     ['Black', 'Green', 'White', 'Pink', 'Yellow', 'Blue', 'Red'],
                     [],
                     ['Green', 'Red', 'Red', 'Red', 'White', 'Black', 'Black'],
                     [],
                     ['Blue', 'Blue', 'Pink', 'Yellow', 'Pink', 'Green', 'Red'],
                     ['Blue', 'Black', 'White', 'Green', 'White', 'Yellow', 'Yellow'],
                     ['White', 'Blue', 'Pink', 'Green', 'Yellow', 'Green', 'Pink'],
                     [],
                     ['Yellow', 'Black', 'White', 'Red', 'Blue', 'Black', 'Pink'],
                     [],
                     []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving one block to the top of each stack
    stack_costs = {0: 10, 1: 8, 2: 12, 3: 3, 4: 5, 5: 11, 6: 5, 7: 12, 8: 3, 9: 3, 10: 11, 11: 6}

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the state is the goal state, where all stacks are sorted
        if all(sorted(stack) == stack for stack in state if stack):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is a valid action
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                    new_state = [list(stack[:]) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the new state based on the cost of moving a block to the top of the 'to_stack'
                    new_cost = g + max(1, stack_costs[to_stack])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Calculate the heuristic cost based on the number of blocks out of order in each stack
                        h = heuristic(new_state)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state):
    # The heuristic is calculated based on the number of blocks out of order in each stack
    # The heuristic is admissible as it underestimates the cost to reach the goal state
    # The heuristic is consistent as the cost of moving a block to the top of a stack is always at least 1, which is the decrease in the heuristic estimate
    h = 0
    for stack in state:
        if stack:
            for i in range(len(stack) - 1):
                if stack[i] > stack[i + 1]:
                    h += 1
    return h


print(a_star())
