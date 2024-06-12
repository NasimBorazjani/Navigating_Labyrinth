
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Black', 'Blue', 'Pink', 'Green', 'Blue', 'Red', 'Red'],
                     ['Yellow', 'White', 'White', 'Black', 'Yellow', 'Green', 'Green'],
                     ['Yellow', 'Pink', 'White', 'Pink', 'Black', 'Red', 'Black'],
                     [],
                     ['Pink', 'Red', 'Blue', 'White', 'Blue', 'Blue', 'Red'],
                     ['Blue', 'Yellow', 'White', 'Pink', 'Pink', 'Green', 'Green'],
                     [],
                     [],
                     ['Yellow', 'Black', 'Yellow', 'White', 'Red', 'Black', 'Green'],
                     [],
                     [],
                     []]
    num_stacks = 12
    stack_capacity = 7
    # Define the cost of moving a block to each stack
    costs = {0: 11, 1: 13, 2: 4, 3: 4, 4: 13, 5: 7, 6: 12, 7: 6, 8: 4, 9: 6, 10: 11, 11: 4}
    # Define the goal state where all stacks are sorted by shade
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
    visited_costs[tuple(tuple(row) for row in initial_state)] = 0

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
                    # Check if transferring a block from the 'from_stack' to the 'to_stack' is valid
                    if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                        new_state = [list(row) for row in state]
                        new_state[from_stack] = new_state[from_stack][:-1]
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(row) for row in new_state)
                        # Calculate the cost of the new state
                        new_cost = g + max(1, costs[from_stack])

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Add the transfer action to the list of actions
                            heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal):
    # The heuristic is the sum of the differences between the current state and the goal state for each stack
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that the cost of moving a block is always 1, which is not always the case
    # The heuristic is consistent because the cost of moving a block to a stack is always at least 1, and the heuristic estimate for the goal state is 0
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += 1
    return h


print(a_star())
