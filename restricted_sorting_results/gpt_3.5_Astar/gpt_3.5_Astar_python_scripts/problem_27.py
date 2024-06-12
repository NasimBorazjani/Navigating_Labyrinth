
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Red', 'Blue', 'Green', 'Yellow'], ['Blue', 'Blue', 'Green', 'Red'], [], [], [], ['Green', 'Red', 'Yellow', 'Yellow']]
    num_stacks = 6
    stack_capacity = 4
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 3, 1: 6, 2: 2, 3: 4, 4: 6, 5: 5}
    # Define the goal state, which is an empty stack
    goal_state = [[], [], [], [], [], []]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if all(not stack for stack in state):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if the transfer is valid, ie the from_stack is not empty and the to_stack is either empty or has blocks of the same shade
                    if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                        new_state = [list(stack[:]) for stack in state]
                        block = new_state[from_stack].pop()
                        new_state[to_stack].append(block)
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the transfer
                        new_cost = g + max(1, stack_costs[from_stack])

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Calculate the heuristic cost
                            h = heuristic(new_state, goal_state, stack_costs)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal, stack_costs):
    # The heuristic is the sum of the costs of moving each block to the correct stack
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that each block can be moved to the correct stack in one move, which is not always the case
    # The heuristic is consistent because the cost of moving a block to the correct stack is always at least 1, which is the decrease in the heuristic estimate if the block is moved to the correct stack
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                h += stack_costs[i]
    return h


print(a_star())
