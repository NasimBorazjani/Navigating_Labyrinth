
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [[], [], [], ['Yellow', 'Green', 'Blue', 'Blue'], ['Red', 'Blue', 'Green', 'Green'], ['Red', 'Red', 'Yellow', 'Yellow']]
    num_stacks = 6
    stack_capacity = 4
    # Define the cost of moving a block to the top of each stack
    move_costs = {0: 5, 1: 3, 2: 5, 3: 6, 4: 5, 5: 7}
    # Define the goal state where each stack is sorted by shade
    goal_state = [[], [], [], ['Blue', 'Blue', 'Green', 'Green'], ['Red', 'Red', 'Yellow', 'Yellow'], ['Red', 'Yellow', 'Green', 'Blue']]

    visited_costs = {}
    visited_costs[tuple(tuple(stack) for stack in initial_state)] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # Check if the current state is the goal state
        if all(stack == goal_state[i] for i, stack in enumerate(state)):
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
                        new_cost = g + move_costs[to_stack]

                        if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                            visited_costs[new_state] = new_cost
                            # Calculate the heuristic cost to reach the goal state
                            h = heuristic(new_state, goal_state, move_costs)
                            heapq.heappush(queue, (new_cost + h, new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal, move_costs):
    # The heuristic is the sum of the costs of moving each block to its correct position in the goal state
    h = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != goal[i][j]:
                # Calculate the cost of moving the block to its correct position
                h += move_costs[i]
    return h


print(a_star())
