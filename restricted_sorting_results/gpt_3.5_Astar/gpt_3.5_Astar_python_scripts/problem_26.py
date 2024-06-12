
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [['Blue', 'Yellow', 'Red', 'Yellow'], ['Green', 'Red', 'Green', 'Red'], ['Blue', 'Green', 'Blue', 'Yellow'], [], [], []]
    num_stacks = 6
    stack_capacity = 4
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 4, 1: 4, 2: 7, 3: 7, 4: 5, 5: 6}
    # Define the goal state, where each stack is sorted by shade
    goal_state = [['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], [], [], []]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if all([stack == goal_stack for stack, goal_stack in zip(state, goal_state)]):
            return actions

        # Generate all possible actions from the current state, which includes transferring a block from one stack to another
        for from_stack in range(num_stacks):
            for to_stack in range(num_stacks):
                if from_stack != to_stack:
                    # Check if transferring a block from the top of the from_stack to the to_stack is valid
                    if state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]):
                        new_state = [list(stack) for stack in state]
                        new_state[to_stack].append(new_state[from_stack].pop())
                        new_state = tuple(tuple(stack) for stack in new_state)
                        # Calculate the cost of the new state
                        new_cost = g + stack_costs[to_stack]

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Calculate the heuristic cost to reach the goal state
                            h = heuristic(new_state, goal_state, stack_costs)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal, stack_costs):
    # The heuristic is the sum of the costs of moving each block to the correct stack
    # This heuristic is admissible because it underestimates the cost to reach the goal state, as it assumes that each block can be moved to the correct stack in one move
    # The heuristic is consistent because the cost of moving a block to the correct stack is always at least 1, which is the decrease in the heuristic estimate
    h = 0
    for stack, goal_stack in zip(state, goal):
        for block, goal_block in zip(stack, goal_stack):
            if block != goal_block:
                h += stack_costs[goal_stack.index(goal_block)]
    return h


print(a_star())
