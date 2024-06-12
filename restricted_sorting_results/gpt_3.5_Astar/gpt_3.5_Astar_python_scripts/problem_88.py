
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Yellow', 'Green', 'White', 'Pink', 'Black', 'Pink', 'Pink'],
                     ['Pink', 'Red', 'White', 'Black', 'Green', 'White', 'Pink'],
                     ['Red', 'Black', 'Green', 'Blue', 'Red', 'Black', 'Yellow'],
                     ['Blue', 'White', 'Blue', 'Blue', 'Black', 'White', 'Blue'],
                     ['Yellow', 'Blue', 'Green', 'Green', 'Red', 'Red', 'Yellow'],
                     [],
                     [],
                     [],
                     ['Black', 'Yellow', 'Red', 'Green', 'Yellow', 'Pink', 'White'],
                     [],
                     [],
                     []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 11, 1: 11, 2: 12, 3: 4, 4: 12, 5: 2, 6: 10, 7: 8, 8: 6, 9: 10, 10: 8, 11: 3}
    # Define the goal state where all stacks are sorted
    goal_state = [['Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black'],
                  ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                  ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                  ['Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink', 'Pink'],
                  ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                  ['White', 'White', 'White', 'White', 'White', 'White', 'White'],
                  ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'],
                  [],
                  [],
                  [],
                  [],
                  []]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if all([state[i] == goal_state[i] for i in range(num_stacks)]):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if transferring a block from the top of the from_stack to the to_stack is valid
                    if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                        new_state = [list(stack[:]) for stack in state]
                        new_state[from_stack] = new_state[from_stack][:-1]
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the transfer
                        new_cost = g + max(1, stack_costs[from_stack])

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Calculate the heuristic cost based on the number of blocks out of order in each stack
                            h = heuristic(new_state, goal_state)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal):
    # The heuristic is the sum of the number of blocks out of order in each stack
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += 1
    return h


print(a_star())
