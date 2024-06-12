
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Black', 'Blue', 'Red', 'White', 'Red', 'Green'],
                     ['Red', 'Black', 'Red', 'Green', 'Blue', 'Black'],
                     ['Black', 'Yellow', 'Yellow', 'White', 'White', 'Yellow'],
                     [], [], ['White', 'Green', 'Green', 'Red', 'Green', 'Yellow'],
                     [], ['Blue', 'Blue', 'Blue', 'Black', 'White', 'Yellow'], [], []]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 3, 1: 8, 2: 5, 3: 10, 4: 8, 5: 2, 6: 3, 7: 4, 8: 11, 9: 3}
    # Define the goal state where all stacks are sorted by shade
    goal_state = [['Black', 'Black', 'Black', 'Black', 'Black', 'Black'],
                  ['Blue', 'Blue', 'Blue', 'Blue', 'Blue', 'Blue'],
                  ['Red', 'Red', 'Red', 'Red', 'Red', 'Red'],
                  ['White', 'White', 'White', 'White', 'White', 'White'],
                  ['Green', 'Green', 'Green', 'Green', 'Green', 'Green'],
                  ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'],
                  [], [], [], []]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if all(stack == goal_stack for stack, goal_stack in zip(state, goal_state)):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                # Check if transferring a block from the 'from_stack' to the 'to_stack' is valid
                if from_stack != to_stack and state[from_stack] and len(state[to_stack]) < stack_capacity and (not state[to_stack] or state[to_stack][-1] == state[from_stack][-1]):
                    new_state = [list(stack) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    # Calculate the cost of the new state
                    new_cost = g + max(1, stack_costs[from_stack])

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Calculate the heuristic cost for the new state
                        h = heuristic(new_state, goal_state, stack_costs)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal_state, stack_costs):
    # The heuristic is the sum of the costs of moving each block to the correct position in the goal state
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that each block can be moved to the correct position with the minimum cost
    # The heuristic is consistent because the cost of moving a block to the correct position is always at least 1, which is the decrease in the heuristic value when moving a block to the correct position
    h = 0
    for stack, goal_stack in zip(state, goal_state):
        for i in range(len(stack)):
            if stack[i] != goal_stack[i]:
                h += stack_costs[i]
    return h


print(a_star())
