
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['White', 'Green', 'Red', 'Blue', 'Red', 'Yellow'],
                     ['Black', 'Black', 'White', 'Blue', 'Green', 'Green'],
                     ['White', 'Blue', 'White', 'Yellow', 'Black', 'Green'],
                     [], [], [], [], ['Green', 'Yellow', 'Red', 'White', 'Blue', 'Black'],
                     ['Yellow', 'Red', 'Blue', 'Red', 'Black', 'Yellow'], []]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 8, 1: 8, 2: 10, 3: 6, 4: 8, 5: 4, 6: 3, 7: 7, 8: 11, 9: 9}
    # Define the goal state where all stacks are sorted by shade
    goal_state = [['Black', 'Black', 'Black', 'Black', 'Black', 'Black'],
                  ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                  ['Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                  ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                  ['White', 'White', 'White', 'White', 'White', 'White'],
                  ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'],
                  [], [], [], []]

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
                    # Check if transferring a block from the 'from_stack' to the 'to_stack' is valid
                    if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                        new_state = [list(stack) for stack in state]
                        new_state[from_stack] = new_state[from_stack][:-1]
                        new_state[to_stack].append(state[from_stack][-1])
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the new state
                        new_cost = g + max(1, stack_costs[from_stack])

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Add the transfer action to the list of actions
                            heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, stack_costs), new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal, stack_costs):
    # The heuristic is the sum of the costs of moving each block to its correct position in the goal state
    # The heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that each block can be moved to its correct position with the minimum cost
    # The heuristic is consistent because the cost of moving a block to its correct position is always at least 1, which is the decrease in the heuristic estimate
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += stack_costs[i]
    return h


print(a_star())
