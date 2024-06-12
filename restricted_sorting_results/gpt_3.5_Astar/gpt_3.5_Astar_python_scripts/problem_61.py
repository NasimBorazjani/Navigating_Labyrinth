
import heapq
import math


def a_star():
    # Define the initial state of the stacks
    initial_state = [[], [], ['Green', 'Red', 'White', 'Green', 'Black', 'White'], [], ['Red', 'Red', 'Yellow', 'White', 'Blue', 'Black'], ['Blue', 'Yellow', 'Red', 'Blue', 'Blue', 'Green'], [], [], ['Black', 'White', 'Black', 'White', 'Yellow', 'Blue'], ['Yellow', 'Black', 'Green', 'Red', 'Green', 'Yellow']]
    num_stacks = 10
    stack_capacity = 6
    # Define the cost of moving a block to the top of each stack
    costs = {0: 7, 1: 11, 2: 8, 3: 10, 4: 5, 5: 6, 6: 10, 7: 10, 8: 4, 9: 11}
    # Define the goal state where all stacks are sorted by shade
    goal_state = [[], ['Black', 'Black', 'Black', 'Black', 'Black'], ['Blue', 'Blue', 'Blue', 'Blue', 'Blue'], ['Green', 'Green', 'Green', 'Green', 'Green'], ['Red', 'Red', 'Red', 'Red', 'Red'], ['White', 'White', 'White', 'White', 'White'], ['Yellow', 'Yellow', 'Yellow', 'Yellow', 'Yellow'], [], [], []]

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
                if from_stack != to_stack and state[from_stack] and (not state[to_stack] or state[from_stack][-1] == state[to_stack][-1]) and len(state[to_stack]) < stack_capacity:
                    new_state = [list(stack) for stack in state]
                    new_state[from_stack].pop()
                    new_state[to_stack].append(state[from_stack][-1])
                    new_state = tuple(tuple(stack) for stack in new_state)
                    new_cost = g + costs[to_stack]

                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        heapq.heappush(queue, (new_cost + heuristic(new_state, goal_state, costs), new_cost, actions + [(from_stack, to_stack)], new_state))

    return None


def heuristic(state, goal_state, costs):
    # The heuristic is the sum of the costs of moving each block to its correct position in the goal state
    h = 0
    for stack, goal_stack in zip(state, goal_state):
        for block, goal_block in zip(stack, goal_stack):
            if block != goal_block:
                h += costs[goal_state.index(goal_stack)]
    return h


print(a_star())
