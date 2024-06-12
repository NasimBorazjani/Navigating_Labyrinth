
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [[], [], ['Red', 'Yellow', 'Black', 'Yellow', 'Green'], ['Red', 'Red', 'Blue', 'Red', 'Black'], [], ['Black', 'Blue', 'Yellow', 'Blue', 'Black'], [], ['Green', 'Green', 'Yellow', 'Blue', 'Green']]
    num_stacks = 8
    stack_capacity = 5
    # Define the cost of moving a block to the top of each stack
    stack_costs = {0: 4, 1: 6, 2: 8, 3: 2, 4: 4, 5: 7, 6: 7, 7: 5}
    # Define the goal state where all stacks are sorted
    goal_state = [[], ['Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red'], ['Yellow', 'Yellow', 'Yellow', 'Yellow'], [], []]

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
                            # Add the transfer action to the list of actions
                            heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state), new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal):
    # The heuristic is the sum of the differences between the current state and the goal state for each stack
    # The heuristic is admissible as it underestimates the cost to reach the goal state
    # The heuristic is consistent as the cost of moving a block to the top of a stack is always at least 1, which is the decrease in the heuristic estimate
    h = 0
    for stack, goal_stack in zip(state, goal):
        h += abs(len(stack) - len(goal_stack))
    return h


print(a_star())
